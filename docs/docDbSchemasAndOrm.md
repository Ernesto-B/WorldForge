# WorldForge Database Schema Design and ORM

## Overview
This schema is designed to support the core features of WorldForge, including users, worlds, campaigns, map regions, session paths, markers, world events, and lore entries. It is designed with relational integrity in mind and optimized for MySQL (or any RDB). To prevent SQL injections and support DB independence, we will also use SQLAlchemy ORM.
[MySQL Docker image](https://hub.docker.com/_/mysql)

- [WorldForge Database Schema Design and ORM](#worldforge-database-schema-design-and-orm)
  - [Overview](#overview)
  - [Users](#users)
  - [Worlds](#worlds)
  - [Campaigns](#campaigns)
  - [Map Regions](#map-regions)
  - [Sessions](#sessions)
  - [Map Markers](#map-markers)
  - [World Events](#world-events)
  - [Lore Entries](#lore-entries)
  - [Relationships and Key Considerations](#relationships-and-key-considerations)
  - [Future Scalability](#future-scalability)
- [SQLAlchemy Models](#sqlalchemy-models)
  - [Querying the models](#querying-the-models)
  - [Example Endpoint](#example-endpoint)


## Users
```sql
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role ENUM('DM', 'Player', 'Collaborator', 'Spectator') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```



## Worlds
```sql
CREATE TABLE worlds (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) UNIQUE NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```



## Campaigns
```sql
CREATE TABLE campaigns (
    id INT PRIMARY KEY AUTO_INCREMENT,
    world_id INT,
    dm_id INT,
    name VARCHAR(100) NOT NULL,
    current_session_number INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (world_id) REFERENCES worlds(id) ON DELETE CASCADE,
    FOREIGN KEY (dm_id) REFERENCES users(id) ON DELETE SET NULL
);
```



## Map Regions
```sql
CREATE TABLE map_regions (
    id INT PRIMARY KEY AUTO_INCREMENT,
    world_id INT,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    coordinates JSON, -- Store polygon or region data as GeoJSON-like structure
    is_revealed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (world_id) REFERENCES worlds(id) ON DELETE CASCADE
);
```



## Sessions
```sql
CREATE TABLE sessions (
    id INT PRIMARY KEY AUTO_INCREMENT,
    campaign_id INT,
    session_number INT NOT NULL,
    path_coordinates JSON, -- Freehand path data as a list of coordinate points
    summary TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (campaign_id) REFERENCES campaigns(id) ON DELETE CASCADE
);
```



## Map Markers
```sql
CREATE TABLE map_markers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    world_id INT,
    user_id INT, -- Optional: If it is a personal marker
    name VARCHAR(100),
    description TEXT,
    coordinates JSON, -- Point location
    is_personal BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (world_id) REFERENCES worlds(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE SET NULL
);
```



## World Events
```sql
CREATE TABLE world_events (
    id INT PRIMARY KEY AUTO_INCREMENT,
    world_id INT,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    pinned_by INT, -- DM who created the event
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (world_id) REFERENCES worlds(id) ON DELETE CASCADE,
    FOREIGN KEY (pinned_by) REFERENCES users(id) ON DELETE SET NULL
);
```



## Lore Entries
```sql
CREATE TABLE lore_entries (
    id INT PRIMARY KEY AUTO_INCREMENT,
    region_id INT,
    title VARCHAR(150) NOT NULL,
    content TEXT,
    created_by INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (region_id) REFERENCES map_regions(id) ON DELETE CASCADE,
    FOREIGN KEY (created_by) REFERENCES users(id) ON DELETE SET NULL
);
```

---

## Relationships and Key Considerations
- **Users** can have different roles (DM, Player, Collaborator, Spectator).
- **Worlds** contain **Campaigns**, **Regions**, **Markers**, and **World Events**.
- **Campaigns** are led by a **DM** and track **Sessions**.
- **Sessions** store freehand paths as JSON for flexibility.
- **Map Regions** and **Map Markers** use JSON for coordinates, supporting free-form maps.
- **World Events** are global announcements pinned by DMs.
- **Lore Entries** are nested under **Map Regions** and can be expanded later with more types (e.g., NPCs, shops).


## Future Scalability
- Add **NPCs**, **Quests**, or **Factions** as separate tables later.
- Consider spatial indexing if the coordinate data becomes complex.
- Possible MongoDB hybrid approach for deeply nested region content if the relational structure becomes too rigid.


# SQLAlchemy Models
```py
from sqlalchemy import Column, Integer, String, Text, ForeignKey, TIMESTAMP, Boolean, JSON, Enum
from sqlalchemy.orm import relationship, declarative_base
import enum
from datetime import datetime

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
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

    campaigns = relationship('CampaignMembership', back_populates='user')


# World Table
class World(Base):
    __tablename__ = 'worlds'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

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
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

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
    joined_at = Column(TIMESTAMP, default=datetime.utcnow)

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
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

    world = relationship('World', back_populates='regions')


# Session Table (Path overlay)
class Session(Base):
    __tablename__ = 'sessions'

    id = Column(Integer, primary_key=True, index=True)
    campaign_id = Column(Integer, ForeignKey('campaigns.id'))
    session_number = Column(Integer, nullable=False)
    path_data = Column(JSON)
    summary = Column(Text)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

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
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

    world = relationship('World', back_populates='markers')


# World Event Table
class WorldEvent(Base):
    __tablename__ = 'world_events'

    id = Column(Integer, primary_key=True, index=True)
    world_id = Column(Integer, ForeignKey('worlds.id'))
    title = Column(String(255))
    description = Column(Text)
    visible_at_session = Column(Integer)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

    world = relationship('World', back_populates='events')
```

## Querying the models
| Goal	| Pattern |
| ----- | ------- |
| Get All Records | db.query(Model).all() |
| Get By ID | db.query(Model).filter(Model.id == id).first() |
| Filter With Multiple Conditions | Query → .filter(Model.field1 == X, Model.field2 == Y) |
| Create Record | db.add(obj) → db.commit() → db.refresh(obj) |
| Update Record | Fetch → Modify → Commit |
| Delete Record	| Fetch → db.delete(obj) → Commit |
| Order By | .order_by(Model.field.asc()) |
| Join Relationships (lazy loading) | Access via .relationship_field after query |

- Consider pagination for larger queries.

## Example Endpoint
```py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.repositories.user_repository import get_user_campaigns

router = APIRouter()

@router.get("/users/{user_id}/campaigns")
def read_user_campaigns(user_id: int, db: Session = Depends(get_db)):
    return get_user_campaigns(db, user_id)
```