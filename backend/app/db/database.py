from pymongo import MongoClient
from core.config import settings
import logging

logger = logging.getLogger(__name__)

try:
    client = MongoClient(settings.MONGO_URI)

    client.admin.command('ping')
    logger.info("MongoDB connection successful.")
    db = client[settings.DATABASE_NAME]
    users_collection = db["users"]

    users_collection.create_index("username", unique=True)
    users_collection.create_index("email", unique=True)
except Exception as e:
    logger.error("MongoDB connection failed.")
    raise

def get_user_by_username(username: str):
    return users_collection.find_one({"username": username})

def get_user_by_email(email: str):
    return users_collection.find_one({"email": email})

def add_user(user_data: dict):
    return users_collection.insert_one(user_data)

def update_user(user_id: str, update_data: dict):
    from bson.objectid import ObjectId
    return users_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": update_data}
    )

def get_user_by_id(user_id: str):
    from bson.objectid import ObjectId
    return users_collection.find_one({"_id": ObjectId(user_id)})

def delete_user(user_id: str):
    from bson.objectid import ObjectId
    return users_collection.delete_one({"_id": ObjectId(user_id)})