from fastapi import FastAPI
from app.db.session import engine
from app.db.base import Base
from app.models import tables

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "AuraGram Backend is running!"}