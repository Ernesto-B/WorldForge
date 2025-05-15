from app.db.models import WorldEvent
from app.core.exceptions import BadRequestError, DatabaseSaveError
from datetime import datetime

def create_world_event(id:int, input_name: str, input_description: str, visible: int, db):
    if len(input_name) > 150:
        raise BadRequestError("Name must be less than 150 characters")
    
    try:
        new_world_event = WorldEvent(
            world_id = id,
            title = input_name,
            description = input_description,
            visible_at_session = visible,
            created_at = datetime.now()
        )

        db.add(new_world_event)
        db.commit()
        db.refresh(new_world_event)

        return new_world_event
    
    except Exception as e:
        raise DatabaseSaveError(str(e))