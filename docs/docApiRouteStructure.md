# Proposed API Route Structure for WorldForge
> [!WARNING]
> NEEDS UPDATING. Cross-reference with `docUxFlowPlan.md` for best idea of features/routes.

## Overview

This API route structure is designed to support the core features of WorldForge, following RESTful principles and aligning with the layered architecture approach. Each route is grouped logically based on resource types, ensuring easy scalability and extensibility.

---

## Authentication

| Method | Endpoint          | Description                         |
| ------ | ----------------- | ----------------------------------- |
| POST   | /api/auth/register| Register a user using Supabase auth |
| POST   | /api/auth/login   | Login a user using Supabase auth    |

---

## Users

| Method | Endpoint                | Description                                |
| ------ | ----------------------  | ------------------------------------------ |
| GET    | /api/users/me           | Get current user profile                   |
| GET    | /api/users/notifications| Get notifications from world and campaigns |
| GET    | /api/users/events       | Get events from world                      |
| GET    | /api/users/{user_id}    | Get details for a specific user            |

---

## Worlds

| Method | Endpoint               | Description        |
| ------ | ---------------------- | ------------------ |
| GET    | /api/worlds            | List all worlds    |
| GET    | /api/worlds/{world_id} | Get world details  |
| POST   | /api/worlds            | Create a new world |

---

## Campaigns

| Method | Endpoint                         | Description                   |
| ------ | -------------------------------- | ----------------------------- |
| GET    | /api/worlds/{world_id}/campaigns | List all campaigns in a world |
| GET    | /api/campaigns/{campaign_id}     | Get campaign details          |
| POST   | /api/worlds/{world_id}/campaigns | Create a new campaign         |
| PATCH  | /api/campaigns/{campaign_id}     | Update campaign settings      |

---

## Map Regions

| Method | Endpoint                       | Description                             |
| ------ | ------------------------------ | --------------------------------------- |
| GET    | /api/worlds/{world_id}/regions | List all visible map regions            |
| GET    | /api/regions/{region_id}       | Get details about a specific map region |
| POST   | /api/worlds/{world_id}/regions | Create a new map region                 |
| PATCH  | /api/regions/{region_id}       | Update a map region                     |
| DELETE | /api/regions/{region_id}       | Delete a map region                     |

---

## Session Paths

| Method | Endpoint                              | Description                                 |
| ------ | ------------------------------------- | ------------------------------------------- |
| GET    | /api/campaigns/{campaign_id}/sessions | Get all sessions and paths for a campaign   |
| GET    | /api/sessions/{session_id}            | Get details and path for a specific session |
| POST   | /api/campaigns/{campaign_id}/sessions | Create a session (DM only)                  |
| PATCH  | /api/sessions/{session_id}            | Update a session path                       |

---

## Map Markers

| Method | Endpoint                       | Description              |
| ------ | ------------------------------ | ------------------------ |
| GET    | /api/worlds/{world_id}/markers | List all visible markers |
| POST   | /api/worlds/{world_id}/markers | Add a new marker         |
| PATCH  | /api/markers/{marker_id}       | Update a marker          |
| DELETE | /api/markers/{marker_id}       | Remove a marker          |

---

## World Events

| Method | Endpoint                      | Description                    |
| ------ | ----------------------------- | ------------------------------ |
| GET    | /api/worlds/{world_id}/events | List all world events          |
| POST   | /api/worlds/{world_id}/events | Create a world event (DM only) |
| PATCH  | /api/events/{event_id}        | Update a world event           |
| DELETE | /api/events/{event_id}        | Remove a world event           |

---

## Lore Entries

| Method | Endpoint                      | Description                             |
| ------ | ----------------------------- | --------------------------------------- |
| GET    | /api/regions/{region_id}/lore | List all lore entries for a region      |
| GET    | /api/lore/{lore_id}           | Get details about a specific lore entry |
| POST   | /api/regions/{region_id}/lore | Create a lore entry                     |
| PATCH  | /api/lore/{lore_id}           | Update a lore entry                     |
| DELETE | /api/lore/{lore_id}           | Delete a lore entry                     |

---

## Key Principles

- **RESTful Structure:** Clear, hierarchical endpoints based on worlds, campaigns, and regions.
- **Extensibility:** Designed to accommodate future additions like quests, NPCs, factions, and more.
- **Role-Based Access:** Certain endpoints (e.g., session creation, event pinning) will be restricted to DMs via middleware.
- **Session Visibility Logic:** Paths and regions will be filtered based on the requesting user’s session progress.

## Future Extensions (Example Routes)

| Method | Endpoint                      | Description           |
| ------ | ----------------------------- | --------------------- |
| GET    | /api/worlds/{world_id}/quests | List quests           |
| POST   | /api/worlds/{world_id}/quests | Create a quest        |
| GET    | /api/regions/{region_id}/npcs | List NPCs in a region |
| POST   | /api/regions/{region_id}/npcs | Create an NPC         |
