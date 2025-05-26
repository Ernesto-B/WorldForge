from app.db.models import WorldTime
from app.core.exceptions import WorldNotFoundError, DatabaseSaveError
from datetime import datetime

def create_world_time(id:int, db):
    try:
        world_time = WorldTime(
            world_id = id,
            world_date = datetime.now()
        )
        
        db.add(world_time)
        db.commit()
        db.refresh(world_time)

        return world_time
        
    except Exception as e: 
        raise DatabaseSaveError(str(e))