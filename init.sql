CREATE DATABASE IF NOT EXISTS worldforge_db;
USE worldforge_db;

CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role ENUM('DM', 'Player', 'Collaborator', 'Spectator') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE worlds (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) UNIQUE NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

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

CREATE TABLE sessions (
    id INT PRIMARY KEY AUTO_INCREMENT,
    campaign_id INT,
    session_number INT NOT NULL,
    path_coordinates JSON, -- Freehand path data as a list of coordinate points
    summary TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (campaign_id) REFERENCES campaigns(id) ON DELETE CASCADE
);

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

