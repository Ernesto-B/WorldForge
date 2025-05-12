import sqlalchemy
from app.core.exceptions import DatabaseQueryError
from app.db.models import Notification, UserCampaignRole
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError


def get_user_notifications(limit, offset, user_participations, db):
    try:
        # make set of all world and campaign id's
        user_campaigns = {item.id for item in user_participations["campaign_info"]}
        user_worlds = {item.id for item in user_participations["world_info"]}

        # get all notifications for worlds and campaigns the user is a part of
        world_notifications = db.query(Notification).filter(Notification.world_id.in_(user_worlds)).limit(limit).offset(offset)
        campaign_notifications = db.query(Notification).filter(Notification.campaign_id.in_(user_campaigns)).limit(limit).offset(offset)

        return {
            "user_world_notifications": world_notifications,
            "user_campaign_notifications": campaign_notifications,
        }

    except SQLAlchemyError as e:
        raise DatabaseQueryError()
