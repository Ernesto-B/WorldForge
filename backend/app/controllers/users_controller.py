from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr
from app.db.supabaseDB import get_db
from app.core.security import get_current_user_id, require_role
from app.services.user import get_user_info
from app.services.notifications import get_user_notifications
from app.services.events import get_world_events

users_controller = APIRouter()


@users_controller.get("/me")
def get_me(user_id: str = Depends(get_current_user_id), db: Session = Depends(get_db)):
    response = get_user_info(user_id, db)
    return response


@users_controller.get("/notifications")
def get_notifications(
    limit: int = 10,
    offset: int = 0,
    user_id: str = Depends(get_current_user_id),
    db: Session = Depends(get_db),
):
    user_participations = get_user_info(user_id, db)
    response = get_user_notifications(limit, offset, user_participations, db)
    return response


@users_controller.get("/events")
def get_events(
    limit: int = 10,
    offset: int = 0,
    user_id: str = Depends(get_current_user_id),
    db: Session = Depends(get_db),
):
    user_participations = get_user_info(user_id, db)
    user_worlds = [world.id for world in user_participations["world_info"]]
    response = get_world_events(limit, offset, user_worlds, db)
    return response


@users_controller.get("/{user_id}")
def get_user(user_id: str, db: Session = Depends(get_db)):
    response = get_user_info(user_id, db)
    # If wanting to restrict info
    # return {
    #     "user_campaigns": response["campaign_names"],
    #     "user_worlds": response["world_names"],
    # }
    return response
