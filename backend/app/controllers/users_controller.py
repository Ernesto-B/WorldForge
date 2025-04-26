from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr
from app.db.supabaseDB import get_db
from app.core.security import require_role
from app.services.user import get_user_info

users_controller = APIRouter()

# TODO: Apply RBAC
@users_controller.get("/me/{user_id}")
def get_me(user_id: str, db: Session = Depends(get_db)):
    response = get_user_info(user_id, db)
    return response
