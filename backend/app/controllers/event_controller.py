from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Any
from pydantic import BaseModel, EmailStr
from app.db.supabaseDB import get_db
from app.core.security import get_current_user_id
from app.services.create_world_event import create_world_event

event_controller = APIRouter()

class new_world_event(BaseModel):
    id: int
    title: str
    description: str
    visible_at_session: int

@event_controller.post("/create_event")
def new_event(
    request: new_world_event,
    db: Session = Depends(get_db)
):
    world_event = create_world_event(
        request.id, 
        request.title, 
        request.description, 
        request.visible_at_session, 
        db)
    return world_event