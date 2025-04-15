from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
# from app.core.supabaseDB import get_db
import app.db.models
from app.services.register import register_user
from app.services.login import login_user
from pydantic import BaseModel, EmailStr

class AuthRequest(BaseModel):
    email: EmailStr
    password: str

auth_controller = APIRouter()

@auth_controller.post("/register")
def register(request: AuthRequest):
    response = register_user(request.email, request.password)
    return({"response": response})


@auth_controller.post("/login")
def login(request: AuthRequest):
    response = login_user(request.email, request.password)
    return({"response": response})

