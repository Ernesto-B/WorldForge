from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr
from pydantic_extra_types.pendulum_dt import Date
from app.services.create_world import create_world

class World(BaseModel):
    id: str
    name: str
    description: str
    created_at: Date

world_controller = APIRouter()

@world_controller.post("/create_world")
def create(request: World):
    response = create_world(request.id, request.name, request.description, request.created_at)
    return response