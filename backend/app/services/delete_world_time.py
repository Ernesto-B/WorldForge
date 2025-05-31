from app.db.models import WorldTime
from app.core.exceptions import WorldNotFoundError, DatabaseSaveError

def delete_world_time(world:int, db):
    try:
        delete = db.query(WorldTime).where(WorldTime.id == world).first()
        if not delete:
            raise WorldNotFoundError("World Not Found")
        
        db.delete(delete)
        db.commit()

        result = ("World Time for world: " + str(delete.id) + ", has been deleted.")

        return result
        
    except Exception as e: 
        raise DatabaseSaveError(str(e))