from app.db.models import World, WorldTime, WorldSettings
from app.core.exceptions import WorldNotFoundError, DatabaseSaveError

def delete_world(world:int, db):
    try:
        delete = db.query(World).where(World.id == world).first()
        if not delete:
            raise WorldNotFoundError("World Not Found")
        
        # delete_settings = db.query(WorldSettings).where(WorldSettings.world_id == world).first
        # if not delete_settings:
        #     raise WorldNotFoundError("World Settings Not Found")
        
        # delete_time = db.query(WorldTime).where(WorldTime.world_id == world).first()
        # if delete_time:
        #     db.delete(delete_time)

        # db.delete(delete_settings)
        db.delete(delete)
        db.commit()

        result = ("World: " + str(delete.id) + ", has been deleted.")

        return result
        
    except Exception as e: 
        raise DatabaseSaveError(str(e))