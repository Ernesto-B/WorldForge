from app.db.models import World
from app.core.exceptions import WorldNotFoundError, DatabaseSaveError

def change_world_description(world_id:int, description: str, db):
    try:
        world = db.query(World).where(World.id == world_id).first()
        if not world:
            raise WorldNotFoundError("World Not Found")
        
        world.description = description
        db.commit()
        db.refresh(world)

        return world.description

    except Exception as e: 
        raise DatabaseSaveError(str(e))