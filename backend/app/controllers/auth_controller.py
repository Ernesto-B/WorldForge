from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
# from app.core.security import
import app.models.models

auth_controller = APIRouter()

@auth_controller.post("/login")
def login():
    ...

@auth_controller.post("/refresh")
def refresh():
    ...
