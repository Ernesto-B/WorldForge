from app.db.models import Campaign
from fastapi import HTTPException
from app.core.exceptions import DatabaseQueryError
from sqlalchemy.exc import SQLAlchemyError

def list_campaign_details(campaign_id, db):
    try:
        campaignInfo = db.query(Campaign).filter(Campaign.id == campaign_id).first()
        details = {
            "name": campaignInfo.name,
            "description": campaignInfo.description,
            "world_id": campaignInfo.world_id,
            "created_at": campaignInfo.created_at,
            "updated_at": campaignInfo.updated_at
        }
        return details
    except DatabaseQueryError as e:
        raise DatabaseQueryError(f"Campaign details not found for campaign_id {campaign_id}: {str(e)}")