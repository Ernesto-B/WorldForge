from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
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
    return response


@auth_controller.post("/login")
def login(request: AuthRequest):
    response = login_user(request.email, request.password)
    return response

