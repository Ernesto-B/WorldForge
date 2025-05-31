from app.db.models import World, WorldSettings
from app.core.exceptions import WorldNotFoundError, DatabaseSaveError
from app.db.models import WorldSettings

def change_settings(settings_id:int, changed_settings, db):
    try:
        settings = db.query(WorldSettings).where(WorldSettings.id == settings_id).first()

        if not settings:
            raise WorldNotFoundError("World Settings not found")

        settings.allow_public_visibility = changed_settings.allow_public_visibility 
        settings.join_method = changed_settings.join_method
        settings.max_campaigns = changed_settings.max_campaigns
        settings.allow_dm_invites = changed_settings.allow_dm_invites
        settings.enable_fog_of_war = changed_settings.enable_fog_of_war
        settings.inter_party_visibility = changed_settings.inter_party_visibility
        settings.spectator_map_visibility = changed_settings.spectator_map_visibility
        settings.show_party_position_globally = changed_settings.show_party_position_globally
    
        db.commit()
        db.refresh(settings)
        
        return settings

    except Exception as e: 
        raise DatabaseSaveError(str(e))


