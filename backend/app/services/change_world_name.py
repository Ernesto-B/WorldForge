from app.db.models import World
from app.core.exceptions import WorldNotFoundError, DatabaseSaveError

def change_world_name(world_id:int, new_name:str, user, db):
    try:
        world = db.query(World).where(World.id == world_id).first()
        if not world:
            raise WorldNotFoundError("World Not Found")
        
        same_name = db.query(World).where(World.created_by == user).where(World.name == new_name).first()
        if same_name:
            raise WorldNotFoundError("Must have a unique name world")
        
        world.name = new_name
        db.commit()
        db.refresh(world)

        return world.name

    except Exception as e: 
        raise DatabaseSaveError(str(e))