from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.register import register_user
from app.services.login import login_user
from pydantic import BaseModel, EmailStr
from app.db.supabaseDB import get_db
from app.db.models import World
from app.core.security import require_role

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

# This demonstrates how to get database connectivity from the bd object using the ORM
# REMOVE THIS... DEV ONLY
@auth_controller.get("/test")
def test(db: Session = Depends(get_db)):
    data = db.query(World).all()
    return data

# This demonstrates how to implement RBAC. Note you must list all permitted roles (DM, Spectator, Player)
# REMOVE THIS... DEV ONLY
@auth_controller.get("/testing/{campaign_id}")
def testing(auth = Depends(require_role("campaign_id", ["DM"]))):
    return {"message": "Access granted"}

