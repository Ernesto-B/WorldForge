from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Any
from pydantic import BaseModel, EmailStr, Json
from app.services.create_world import create_world
from app.services.search_world_id import search_world_id
from app.services.update_world_settings import change_settings
from app.db.supabaseDB import get_db
from app.db.models import World
from app.core.security import get_current_user_id

world_controller = APIRouter()

class newWorld(BaseModel):
    name: str
    description: str

class world_search_id(BaseModel):
    search: int

class settings(BaseModel):
    allow_public_visibility: bool
    join_method: str
    max_campaigns: int
    allow_dm_invites: bool
    enable_fog_of_war: bool
    inter_party_visibility: bool
    spectator_map_visibility: bool
    show_party_position_globally: bool

class new_world_settings(BaseModel):
    settings_id: int
    changed_settings: settings


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

@world_controller.post("/update_world_settings")
def update_world_settings(
    request: new_world_settings,
    db: Session = Depends(get_db)
):
    data = change_settings(request.settings_id, request.changed_settings, db)    
    return data

