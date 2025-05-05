from fastapi import HTTPException
from app.core.exceptions import DatabaseQueryError
from app.db.models import WorldEvent
from sqlalchemy.exc import SQLAlchemyError


def get_world_events(limit, offset, user_worlds, db):
    try:
        world_events = db.query(WorldEvent).filter(WorldEvent.id.in_(user_worlds)).limit(limit).offset(offset)
        return world_events
    except SQLAlchemyError as e:
        raise DatabaseQueryError()

