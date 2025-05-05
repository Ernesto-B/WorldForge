from app.db.models import World
from app.core.exceptions import BadRequestError, DatabaseSaveError

def create_world(input_name: str, input_description: str, user_id, db):
    if len(input_name) > 100:
        raise BadRequestError("Name must be less than 100 characters")
    
    try:
        new_world = World(
            name = input_name,
            description = input_description,
            created_by = user_id
        )

        db.add(new_world)
        db.commit()
        db.refresh(new_world)

        return {
            "world": new_world.id
        }
    
    except Exception as e: 
        raise DatabaseSaveError(str(e))