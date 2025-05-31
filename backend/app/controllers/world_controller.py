from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Any
from pydantic import BaseModel, EmailStr
from app.services.create_world import create_world
from app.services.change_world_name import change_world_name
from app.services.change_world_description import change_world_description
from app.services.search_world_id import search_world_id
from app.services.delete_world import delete_world
from app.services.update_world_settings import change_settings
from app.services.create_world_time import create_world_time
from app.services.change_world_time import change_world_time
from app.services.delete_world_time import delete_world_time
from app.db.supabaseDB import get_db
from app.core.security import get_current_user_id

world_controller = APIRouter()

class new_world(BaseModel):
    name: str
    description: str

class world_search_id(BaseModel):
    world_id: int

class new_input(BaseModel):
    id: int
    input: str

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
    settings: settings

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# Create world

@world_controller.post("/create_world")
def new_world(
    request: new_world,
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
    found_world = search_world_id(request.world_id, db)
    return found_world

@world_controller.post("/update_world_name")
def update_world_name(
    request: new_input,
    user_id: str = Depends(get_current_user_id),
    db: Session = Depends(get_db)
):
    world = change_world_name(request.id, request.input, user_id, db)
    return world

@world_controller.post("/update_world_description")
def update_world_name(
    request: new_input,
    db: Session = Depends(get_db)
):
    world = change_world_description(request.id, request.input, db)
    return world

@world_controller.delete("/delete_world")
def remove_world(
    request: world_search_id,
    db: Session = Depends(get_db)
):
    deleted = delete_world(request.world_id, db)
    return deleted

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# World Settings

@world_controller.post("/update_world_settings")
def update_world_settings(
    request: new_world_settings,
    db: Session = Depends(get_db)
):
    data = change_settings(request.settings_id, request.settings, db)    
    return data

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# World Time

@world_controller.post("/create_world_time")
def new_world_time(
    request: world_search_id,
    db: Session = Depends(get_db)
):
    world_time = create_world_time(request.world_id, db)
    return world_time

@world_controller.post("/update_world_time")
def update_world_time(
    request: new_input,
    db: Session = Depends(get_db)
):
    world_time = change_world_time(request.id, request.input, db)
    return world_time

@world_controller.delete("/delete_world_time")
def remove_world_time(
    request: world_search_id,
    db: Session = Depends(get_db)
):
    deleted = delete_world_time(request.world_id, db)
    return deleted