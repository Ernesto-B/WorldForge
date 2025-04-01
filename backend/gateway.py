from fastapi import FastAPI

app = FastAPI()

# core routers
app.include_router(auth_controller.router, prefix="/api/auth", tags=["auth"])
app.include_router(users_controller.router, prefix="/api/users", tags=["users"])
app.include_router(worlds_controller.router, prefix="/api/worlds", tags=["worlds"])

# campaigns
app.include_router(campaigns_controller.router, prefix="/api/campaigns", tags=["campaigns"])
app.include_router(campaigns_controller.router, prefix="/api/worlds/{world_id}/campaigns", tags=["campaigns"])

# regions
app.include_router(mapRegions_controller.router, prefix="/api/regions", tags=["regions"])
app.include_router(mapRegions_controller.router, prefix="/api/worlds/{world_id}/regions", tags=["regions"])

# sessions
app.include_router(sessions_controller.router, prefix="/api/sessions", tags=["sessions"])
app.include_router(sessions_controller.router, prefix="/api/campaigns/{campaign_id}/sessions", tags=["sessions"])

# markers
app.include_router(markers_controller.router, prefix="/api/markers", tags=["markers"])
app.include_router(markers_controller.router, prefix="/api/worlds/{world_id}/markers", tags=["markers"])

# world events
app.include_router(events_controller.router, prefix="/api/events", tags=["events"])
app.include_router(events_controller.router, prefix="/api/worlds/{world_id}/events", tags=["events"])

# lore entries
app.include_router(lore_controller.router, prefix="/api/lore", tags=["lore"])
app.include_router(lore_controller.router, prefix="/api/regions/{region_id}/lore", tags=["lore"])


@app.get("/")
async def root():
    return {"message:" : "Root"}


