from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr
from pydantic_extra_types.pendulum_dt import Date
from app.services.create_world import create_world
from app.services.search_world_id import search_world_id
from app.db.supabaseDB import get_db
from app.db.models import World
from app.core.security import get_current_user_id

world_controller = APIRouter()

class newWorld(BaseModel):
    name: str
    description: str

class world_search_id(BaseModel):
    search: int

@world_controller.post("/create_world")
def new_world(
    request: newWorld,
    user_id: str = Depends(get_current_user_id),
    db: Session = Depends(get_db)
):
    data = create_world(request.name, request.description, user_id, db)
    return data

@world_controller.get("/get_world")
def get_world_by_id(
    request: world_search_id,
    db: Session = Depends(get_db)
):
    found_world = search_world_id(request.search, db)
    return found_world

# = = = = = = = = = = = = = = = = = 
# World Settings

