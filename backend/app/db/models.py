from sqlalchemy import Column, Integer, String, Text, ForeignKey, TIMESTAMP, Boolean, JSON, Enum
from sqlalchemy.orm import relationship, declarative_base
import enum
import datetime

Base = declarative_base()

# ENUMS for roles
class UserRole(enum.Enum):
    DM = 'DM'
    Player = 'Player'
    Collaborator = 'Collaborator'
    Spectator = 'Spectator'

class CampaignRole(enum.Enum):
    Player = 'Player'
    Collaborator = 'Collaborator'
    Spectator = 'Spectator'


# User Table
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False)
    username = Column(String(100), nullable=False)
    role = Column(Enum(UserRole), nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.datetime.now(datetime.timezone.utc))

    campaigns = relationship('CampaignMembership', back_populates='user')


# World Table
class World(Base):
    __tablename__ = 'worlds'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    created_at = Column(TIMESTAMP, default=datetime.datetime.now(datetime.timezone.utc))

    campaigns = relationship('Campaign', back_populates='world')
    regions = relationship('MapRegion', back_populates='world')
    markers = relationship('MapMarker', back_populates='world')
    events = relationship('WorldEvent', back_populates='world')


# Campaign Table
class Campaign(Base):
    __tablename__ = 'campaigns'

    id = Column(Integer, primary_key=True, index=True)
    world_id = Column(Integer, ForeignKey('worlds.id'))
    dm_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String(255), nullable=False)
    current_session = Column(Integer, default=1)
    created_at = Column(TIMESTAMP, default=datetime.datetime.now(datetime.timezone.utc))

    world = relationship('World', back_populates='campaigns')
    memberships = relationship('CampaignMembership', back_populates='campaign')
    sessions = relationship('Session', back_populates='campaign')


# Campaign Membership Table (Players, Spectators, Collaborators)
class CampaignMembership(Base):
    __tablename__ = 'campaign_memberships'

    id = Column(Integer, primary_key=True, index=True)
    campaign_id = Column(Integer, ForeignKey('campaigns.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    role = Column(Enum(CampaignRole))
    joined_at = Column(TIMESTAMP, default=datetime.datetime.now(datetime.timezone.utc))

    campaign = relationship('Campaign', back_populates='memberships')
    user = relationship('User', back_populates='campaigns')


# Map Region Table
class MapRegion(Base):
    __tablename__ = 'map_regions'

    id = Column(Integer, primary_key=True, index=True)
    world_id = Column(Integer, ForeignKey('worlds.id'))
    name = Column(String(255), nullable=False)
    description = Column(Text)
    coordinates = Column(JSON)
    is_revealed = Column(Boolean, default=False)
    revealed_at_session = Column(Integer, nullable=True)
    created_at = Column(TIMESTAMP, default=datetime.datetime.now(datetime.timezone.utc))

    world = relationship('World', back_populates='regions')


# Session Table (Path overlay)
class Session(Base):
    __tablename__ = 'sessions'

    id = Column(Integer, primary_key=True, index=True)
    campaign_id = Column(Integer, ForeignKey('campaigns.id'))
    session_number = Column(Integer, nullable=False)
    path_data = Column(JSON)
    summary = Column(Text)
    created_at = Column(TIMESTAMP, default=datetime.datetime.now(datetime.timezone.utc))

    campaign = relationship('Campaign', back_populates='sessions')


# Map Marker Table
class MapMarker(Base):
    __tablename__ = 'map_markers'

    id = Column(Integer, primary_key=True, index=True)
    world_id = Column(Integer, ForeignKey('worlds.id'))
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    name = Column(String(255))
    description = Column(Text)
    coordinates = Column(JSON)
    created_at = Column(TIMESTAMP, default=datetime.datetime.now(datetime.timezone.utc))

    world = relationship('World', back_populates='markers')


# World Event Table
class WorldEvent(Base):
    __tablename__ = 'world_events'

    id = Column(Integer, primary_key=True, index=True)
    world_id = Column(Integer, ForeignKey('worlds.id'))
    title = Column(String(255))
    description = Column(Text)
    visible_at_session = Column(Integer)
    created_at = Column(TIMESTAMP, default=datetime.datetime.now(datetime.timezone.utc))

    world = relationship('World', back_populates='events')


