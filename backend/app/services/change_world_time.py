from app.db.models import WorldTime
from app.core.exceptions import WorldNotFoundError, DatabaseSaveError
from datetime import datetime

def change_world_time(id:int, new_time:str, db):
    try:
        world_time = db.query(WorldTime).where(WorldTime.id == id).first()
        if not world_time:
            raise WorldNotFoundError("World Time Not Found")
        
        world_time.world_date = new_time
        world_time.last_updated = datetime.now()

        db.commit()
        db.refresh(world_time)

        return world_time

    except Exception as e:
        raise DatabaseSaveError(str(e))