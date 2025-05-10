from app.db.models import World
from app.core.exceptions import BadRequestError, DatabaseSaveError

def search_world_id(search_id:int, db):
    try:
        result = db.query(World).filter(World.id == search_id).first()

        return result
    
    except Exception as e: 
        raise DatabaseSaveError(str(e))