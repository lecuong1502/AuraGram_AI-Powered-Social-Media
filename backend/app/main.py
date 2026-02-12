import json
import logging
from datetime import datetime, timezone, timedelta
from typing import List

from bson import json_util, ObjectId
from fastapi import Depends, FastAPI, Header, HTTPException, Query, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt

from core.auth import (
    authenticate_user,
    create_access_token,
    get_current_active_user,
    get_password_hash,
    has_role,
)

from core.config import settings
from db.database import (
    add_user,
    delete_user,
    get_user_by_email,
    get_user_by_id,
    get_user_by_username,
    update_user,
)

from models.users import Token, User, UserCreate, UserUpdate

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Auht API",
    description="Auth API with FastAPI and MongoDB Atlas",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def parse_json(data):
    return json.loads(json_util.dumps(data))

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unexpected error: {str(exc)}")
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "Server error. Please try again later."}
    )

@app.get("/")
async def root():
    return {"message": "Welcome to Auth API", "version": "1.0.0"}

@app.post("/register", response_model=dict, status_code=status.HTTP_201_CREATED)
async def register_user(user: UserCreate):
    db_user = get_user_by_username(user.username)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="username already registered"
        )
    
    db_user = get_user_by_email(user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    hashed_password = get_password_hash(user.password)
    user_data = {
        "username": user.username,
        "email": user.email,
        "hashed_password": hashed_password,
        "full_name": user.full_name,
        "disabled": False,
        "created_at": datetime.utcnow(),
        "roles": ["user"]
    }

    try:
        result = add_user(user_data)
        logger.info(f"New user created: {user.username}")
        return {
            "message": "User created successfully", 
            "user_id": str(result.inserted_id)
        }
    except Exception as e:
        logger.error(f"User creation error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error creating user"
        )
    
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        logger.warning(f"Failed login attempt: {form_data.username}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    user_roles = user.get("roles", ["users"])

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"], "roles": user_roles}, 
        expires_delta=access_token_expires
    )

    update_user(str(user["_id"])), {"last_login": datetime.now(timezone.utc)}

    logger.info(f"User logged in: {form_data.username}")
    return {"access_token": access_token, "token_type": "bearer"}

@app.put("/users/me", response_model=dict)
async def update_user_me(user_update: UserUpdate, current_user = Depends(get_current_active_user)):
    user_id = str(current_user["_id"])
    update_data = user_update.model_dump(exclude_unset=True)

    if "password" in update_data and update_data["password"]:
        update_data["hashed_password"] = get_password_hash(update_data["password"])
        del update_data["password"]

    result = update_user(user_id, update_data)
    
    if result.modified_count == 1:
        logger.info(f"User updated: {current_user['username']}")
        return {"message": "User information updated successfully"}
    else:
        logger.warning(f"User update failed: {current_user['username']}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Failed to update user information"
        )
    
@app.get("/admin/users", response_model=List[dict])
async def list_all_users(current_user = Depends(has_role(["admin"]))):
    from db.database import db
    users = list(db.users.find({}, {"hashed_password": 0}))
    return parse_json(users)

@app.get("/users/me", response_model=dict)
async def read_users_me(current_user: dict = Depends(get_current_active_user)):
    return {
        "username": current_user["username"],
        "email": current_user["email"],
        "full_name": current_user.get("full_name"),
        "roles": current_user.get("roles", ["user"])
    }

@app.get("/protected-resource")
async def protected_resource(current_user: dict = Depends(get_current_active_user)):
    return {
        "message": "This is a protected resource",
        "user": current_user["username"]
    }

@app.get("/admin-resource")
async def admin_resource(current_user = Depends(has_role(["admin"]))):
    return {
        "message": "This resource is only accessible to admins",
        "user": current_user["username"],
        "roles": current_user.get("roles", []),
        "timestamp": datetime.now(timezone.utc)
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)