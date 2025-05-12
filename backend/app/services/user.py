from app.db.models import Campaign, UserCampaignRole, World
from fastapi import HTTPException
from app.core.exceptions import DatabaseQueryError, UserNotFoundError
from sqlalchemy.exc import SQLAlchemyError

def get_user_info(user_id: str, db):
    try:
        # load user's roles in every campaign
        user_involvements = db.query(UserCampaignRole).filter_by(user_id = user_id).all()

        if not user_involvements:
            raise UserNotFoundError()

        # extract campaign ID's
        user_campaign_ids = {item.campaign_id for item in user_involvements}

        # load campaign object
        user_campaigns = db.query(Campaign).filter(Campaign.id.in_(user_campaign_ids)).all()

        # extract campaign name
        user_campaign_names = [c.name for c in user_campaigns]

        # extract world ID's
        user_world_ids = {item.world_id for item in user_involvements}

        # load world objects
        user_worlds = db.query(World).filter(World.id.in_(user_world_ids)).all()

        # extract world name
        user_world_names = [w.name for w in user_worlds]

        return {
            "campaign_names": user_campaign_names,
            "campaign_info": user_campaigns,
            "world_names": user_world_names,
            "world_info": user_worlds,
        }

    except SQLAlchemyError as e:
        raise  DatabaseQueryError()
