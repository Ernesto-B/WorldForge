from fastapi import HTTPException
from app.db.models import WorldEvent


def get_world_events(limit, offset, user_worlds, db):
    try:
        world_events = db.query(WorldEvent).filter(WorldEvent.id.in_(user_worlds)).limit(limit).offset(offset)
        return world_events
    except Exception as e:
        raise HTTPException(500, str(e))

