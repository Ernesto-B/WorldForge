from app.db.models import World, WorldSettings
from app.core.exceptions import BadRequestError, DatabaseSaveError

def create_world(input_name: str, input_description: str, user_id, db):
    if len(input_name) > 100:
        raise BadRequestError("Name must be less than 100 characters")
    
    try:
        #make new world
        new_world = World(
            name = input_name,
            description = input_description,
            created_by = user_id
        )

        db.add(new_world)
        db.commit()
        db.refresh(new_world)

        #Attach world setting to new world
        new_world_settings = WorldSettings(
            world_id = new_world.id
        )

        db.add(new_world_settings)
        db.commit()
        db.refresh(new_world_settings)

        return {
            "world": new_world.id,
            "world_settings": new_world_settings.id
        }
    
    except Exception as e: 
        raise DatabaseSaveError(str(e))