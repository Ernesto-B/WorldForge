from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Any
from pydantic import BaseModel
from app.db.supabaseDB import get_db
from app.services.list_campaigns import list_world_campaigns
from app.services.campaign_details import list_campaign_details

campaign_controller = APIRouter()

class list_campaigns_request(BaseModel):
    world_id: int
    
@campaign_controller.get("/list_campaigns")
def list_campaigns(
    request: list_campaigns_request,
    db: Session = Depends(get_db)
):
    response = list_world_campaigns(request, db)
    return response

class get_campaign_details_request(BaseModel):
    campaign_id: int
    
@campaign_controller.get("/get_campaign_details")
def get_campaign_details(
    request: get_campaign_details_request,
    db: Session = Depends(get_db)
): 
    response = list_campaign_details(request, db)
    return response


