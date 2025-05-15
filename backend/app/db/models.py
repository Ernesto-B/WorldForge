from sqlalchemy import (
    Column, String, Integer, Boolean, ForeignKey, Text, DateTime, JSON, UniqueConstraint
)
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime
from app.db.supabaseDB import Base

class World(Base):
    __tablename__ = 'worlds'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.now)
    created_by = Column(UUID, nullable=True)

    campaigns = relationship("Campaign", back_populates="world", cascade="all, delete-orphan")
    regions = relationship("MapRegion", back_populates="world", cascade="all, delete-orphan")
    events = relationship("WorldEvent", back_populates="world", cascade="all, delete-orphan")
    markers = relationship("MapMarker", back_populates="world", cascade="all, delete-orphan")
    settings = relationship("WorldSettings", back_populates="world", uselist=False, cascade="all, delete-orphan")
    notifications = relationship("Notification", back_populates="world", cascade="all, delete-orphan")
    time = relationship("WorldTime", back_populates="world", uselist=False, cascade="all, delete-orphan")


class WorldSettings(Base):
    __tablename__ = 'world_settings'

    id = Column(Integer, primary_key=True)
    world_id = Column(Integer, ForeignKey('worlds.id', ondelete='CASCADE'), unique=True)
    allow_public_visibility = Column(Boolean, default=False)
    join_method = Column(String(20))
    max_campaigns = Column(Integer, default=5)
    allow_dm_invites = Column(Boolean, default=True)
    enable_fog_of_war = Column(Boolean, default=True)
    inter_party_visibility = Column(Boolean, default=False)
    spectator_map_visibility = Column(Boolean, default=True)
    show_party_position_globally = Column(Boolean, default=False)

    world = relationship("World", back_populates="settings")


class Campaign(Base):
    __tablename__ = 'campaigns'

    id = Column(Integer, primary_key=True)
    world_id = Column(Integer, ForeignKey('worlds.id', ondelete='CASCADE'))
    dm_id = Column(UUID, ForeignKey('auth.users.id', ondelete='SET NULL'))
    name = Column(String(100), nullable=False)
    current_session_number = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.now)

    world = relationship("World", back_populates="campaigns")
    sessions = relationship("Session", back_populates="campaign", cascade="all, delete-orphan")
    positions = relationship("PartyPosition", back_populates="campaign", cascade="all, delete-orphan")
    invites = relationship("CampaignInvite", back_populates="campaign", cascade="all, delete-orphan")
    notifications = relationship("Notification", back_populates="campaign", cascade="all, delete-orphan")
    roles = relationship("UserCampaignRole", back_populates="campaign", cascade="all, delete-orphan")


class MapRegion(Base):
    __tablename__ = 'map_regions'

    id = Column(Integer, primary_key=True)
    world_id = Column(Integer, ForeignKey('worlds.id', ondelete='CASCADE'))
    name = Column(String(100), nullable=False)
    description = Column(Text)
    coordinates = Column(JSONB)
    is_revealed = Column(Boolean, default=False)
    revealed_at_session = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.now)

    world = relationship("World", back_populates="regions")
    lore_entries = relationship("LoreEntry", back_populates="region")


class Session(Base):
    __tablename__ = 'sessions'

    id = Column(Integer, primary_key=True)
    campaign_id = Column(Integer, ForeignKey('campaigns.id', ondelete='CASCADE'))
    session_number = Column(Integer, nullable=False)
    path_data = Column(JSONB)
    summary = Column(Text)
    created_at = Column(DateTime, default=datetime.now)

    campaign = relationship("Campaign", back_populates="sessions")
    positions = relationship("PartyPosition", back_populates="session")


class MapMarker(Base):
    __tablename__ = 'map_markers'

    id = Column(Integer, primary_key=True)
    world_id = Column(Integer, ForeignKey('worlds.id', ondelete='CASCADE'))
    created_by = Column(UUID, ForeignKey('auth.users.id', ondelete='SET NULL'))
    name = Column(String(100))
    description = Column(Text)
    coordinates = Column(JSONB)
    is_personal = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now)

    world = relationship("World", back_populates="markers")


class WorldEvent(Base):
    __tablename__ = 'world_events'

    id = Column(Integer, primary_key=True)
    world_id = Column(Integer, ForeignKey('worlds.id', ondelete='CASCADE'))
    title = Column(String(150), nullable=False)
    description = Column(Text)
    visible_at_session = Column(Integer)
    created_at = Column(DateTime, default=datetime.now)

    world = relationship("World", back_populates="events")


class LoreEntry(Base):
    __tablename__ = 'lore_entries'

    id = Column(Integer, primary_key=True)
    region_id = Column(Integer, ForeignKey('map_regions.id', ondelete='CASCADE'))
    title = Column(String(150), nullable=False)
    content = Column(Text)
    created_by = Column(UUID, ForeignKey('auth.users.id', ondelete='SET NULL'))
    created_at = Column(DateTime, default=datetime.now)

    region = relationship("MapRegion", back_populates="lore_entries")


class UserCampaignRole(Base):
    __tablename__ = 'user_campaign_roles'
    __table_args__ = (UniqueConstraint('user_id', 'campaign_id'),)

    id = Column(Integer, primary_key=True)
    user_id = Column(UUID, ForeignKey('auth.users.id', ondelete='CASCADE'), nullable=False)
    world_id = Column(Integer, ForeignKey('worlds.id', ondelete='CASCADE'), nullable=False)
    campaign_id = Column(Integer, ForeignKey('campaigns.id', ondelete='CASCADE'), nullable=False)
    role = Column(String(32), nullable=False)
    joined_at = Column(DateTime, default=datetime.now)

    campaign = relationship("Campaign", back_populates="roles")


class Notification(Base):
    __tablename__ = 'notifications'

    id = Column(Integer, primary_key=True)
    world_id = Column(Integer, ForeignKey('worlds.id', ondelete='CASCADE'))
    campaign_id = Column(Integer, ForeignKey('campaigns.id', ondelete='CASCADE'))
    user_id = Column(UUID, ForeignKey('auth.users.id', ondelete='SET NULL'))
    title = Column(String(200))
    message = Column(Text)
    type = Column(String(30))
    created_at = Column(DateTime, default=datetime.now)

    world = relationship("World", back_populates="notifications")
    campaign = relationship("Campaign", back_populates="notifications")


class PartyPosition(Base):
    __tablename__ = 'party_positions'

    id = Column(Integer, primary_key=True)
    campaign_id = Column(Integer, ForeignKey('campaigns.id', ondelete='CASCADE'))
    session_id = Column(Integer, ForeignKey('sessions.id', ondelete='CASCADE'))
    position = Column(JSONB, nullable=False)
    created_at = Column(DateTime, default=datetime.now)

    campaign = relationship("Campaign", back_populates="positions")
    session = relationship("Session", back_populates="positions")


class WorldTime(Base):
    __tablename__ = 'world_time'

    id = Column(Integer, primary_key=True)
    world_id = Column(Integer, ForeignKey('worlds.id', ondelete='CASCADE'), unique=True, nullable=False)
    world_date = Column(String(100))
    last_updated = Column(DateTime, default=datetime.now)

    world = relationship("World", back_populates="time")


class CampaignInvite(Base):
    __tablename__ = 'campaign_invites'

    id = Column(Integer, primary_key=True)
    campaign_id = Column(Integer, ForeignKey('campaigns.id', ondelete='CASCADE'))
    user_id = Column(UUID, ForeignKey('auth.users.id', ondelete='CASCADE'))
    invited_by = Column(UUID)
    status = Column(String(20), default='pending')
    created_at = Column(DateTime, default=datetime.now)

    campaign = relationship("Campaign", back_populates="invites")

