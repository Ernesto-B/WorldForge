# WorldForge Database Schema Design and ORM

## Overview
This schema is designed to support the core features of WorldForge, including users, worlds, campaigns, map regions, session paths, markers, world events, and lore entries. It is designed with relational integrity in mind and optimized for MySQL (or any RDB). To prevent SQL injections and support DB independence, we will also use SQLAlchemy ORM.

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

## Worlds
```sql
CREATE TABLE worlds (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) UNIQUE NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
## World Settings
```
CREATE TABLE world_settings (
    id SERIAL PRIMARY KEY,
    world_id INT UNIQUE NOT NULL REFERENCES worlds(id) ON DELETE CASCADE,
    allow_public_visibility BOOLEAN DEFAULT FALSE,
    join_method VARCHAR(20) CHECK (join_method IN ('invite', 'request')),
    max_campaigns INT DEFAULT 5,
    allow_dm_invites BOOLEAN DEFAULT TRUE,
    enable_fog_of_war BOOLEAN DEFAULT TRUE,
    inter_party_visibility BOOLEAN DEFAULT FALSE,
    spectator_map_visibility BOOLEAN DEFAULT TRUE,
    show_party_position_globally BOOLEAN DEFAULT FALSE
);
```


## Campaigns
```sql
CREATE TABLE campaigns (
    id SERIAL PRIMARY KEY,
    world_id INT,
    dm_id UUID,
    name VARCHAR(100) NOT NULL,
    current_session_number INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (world_id) REFERENCES worlds(id) ON DELETE CASCADE,
    FOREIGN KEY (dm_id) REFERENCES auth.users(id) ON DELETE SET NULL
);
```



## Map Regions
```sql
CREATE TABLE map_regions (
    id SERIAL PRIMARY KEY,
    world_id INT,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    coordinates JSONB,
    is_revealed BOOLEAN DEFAULT FALSE,
    revealed_at_session INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (world_id) REFERENCES worlds(id) ON DELETE CASCADE
);
```



## Sessions
```sql
CREATE TABLE sessions (
    id SERIAL PRIMARY KEY,
    campaign_id INT,
    session_number INT NOT NULL,
    path_data JSONB,
    summary TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (campaign_id) REFERENCES campaigns(id) ON DELETE CASCADE
);
```



## Map Markers
```sql
CREATE TABLE map_markers (
    id SERIAL PRIMARY KEY,
    world_id INT,
    created_by UUID,
    name VARCHAR(100),
    description TEXT,
    coordinates JSONB,
    is_personal BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (world_id) REFERENCES worlds(id) ON DELETE CASCADE,
    FOREIGN KEY (created_by) REFERENCES auth.users(id) ON DELETE SET NULL
);
```



## World Events
```sql
CREATE TABLE world_events (
    id SERIAL PRIMARY KEY,
    world_id INT,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    visible_at_session INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (world_id) REFERENCES worlds(id) ON DELETE CASCADE
);
```



## Lore Entries
```sql
CREATE TABLE lore_entries (
    id SERIAL PRIMARY KEY,
    region_id INT,
    title VARCHAR(150) NOT NULL,
    content TEXT,
    created_by UUID,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (region_id) REFERENCES map_regions(id) ON DELETE CASCADE,
    FOREIGN KEY (created_by) REFERENCES auth.users(id) ON DELETE SET NULL
);
```

## User Campaign Roles (Join Table)
```sql
CREATE TABLE user_campaign_roles (
  id SERIAL PRIMARY KEY,
  user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  world_id INTEGER NOT NULL REFERENCES worlds(id) ON DELETE CASCADE,
  campaign_id INTEGER NOT NULL REFERENCES campaigns(id) ON DELETE CASCADE,
  role VARCHAR(32) NOT NULL CHECK (role IN ('Creator', 'Member', 'Pending')),
  joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UNIQUE(user_id, campaign_id)
);
```

## Notifications
```sql
CREATE TABLE notifications (
    id SERIAL PRIMARY KEY,
    world_id INT,
    campaign_id INT,
    user_id UUID,
    title VARCHAR(200),
    message TEXT,
    type VARCHAR(30),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (world_id) REFERENCES worlds(id) ON DELETE CASCADE,
    FOREIGN KEY (campaign_id) REFERENCES campaigns(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES auth.users(id) ON DELETE SET NULL
);
```

## Party Positions
```sql
CREATE TABLE party_positions (
    id SERIAL PRIMARY KEY,
    campaign_id INT REFERENCES campaigns(id) ON DELETE CASCADE,
    session_id INT REFERENCES sessions(id) ON DELETE CASCADE,
    position JSONB NOT NULL,  -- e.g., { "x": 105, "y": 240 } or map coordinate ID
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```


## World Time
```sql
CREATE TABLE world_time (
    id SERIAL PRIMARY KEY,
    world_id INT UNIQUE NOT NULL REFERENCES worlds(id) ON DELETE CASCADE,
    world_date VARCHAR(100), -- (e.g. "Year 142, Winter")
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Campaign Invites
```sql
CREATE TABLE campaign_invites (
    id SERIAL PRIMARY KEY,
    campaign_id INT NOT NULL REFERENCES campaigns(id) ON DELETE CASCADE,
    user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
    invited_by UUID,
    status VARCHAR(20) CHECK (status IN ('pending', 'accepted', 'rejected')) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
---

## Future Scalability
- Add **NPCs**, **Quests**, or **Factions** as separate tables later.
- Consider spatial indexing if the coordinate data becomes complex.
- Possible MongoDB hybrid approach for deeply nested region content if the relational structure becomes too rigid.


## Querying the models using SQLAlchemy
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
    return get_user_campaigns(db, user_id)  # Call function in service file


# Using ORM example
# Import desired table model class from models file.
from app.db.models import WorldSettings
@router.get("/anotherTest/{world_id}")
def get_join_method(db: Session = Depends(get_db)):
    response = db.query(WorldSettings).filter_by(world_id=world_id).first()
```
