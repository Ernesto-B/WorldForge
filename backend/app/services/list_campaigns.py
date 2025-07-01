from fastapi import HTTPException
from app.core.exceptions import CampaignNotFoundError
from app.db.models import World, Campaign
from sqlalchemy.exc import SQLAlchemyError

def list_world_campaigns(world_id, db):
    try:
        campaigns = db.query(World).filter(Campaign.world_id == world_id)
        return campaigns
    except CampaignNotFoundError as e:
        raise CampaignNotFoundError(f"Campaigns not found for world_id {world_id}: {str(e)}")
    