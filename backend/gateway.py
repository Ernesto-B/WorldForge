from fastapi import FastAPI

app = FastAPI()

app.include_router(auth_controller.router, prefix="/api/auth", tags=["auth"])
app.include_router(users_controller.router, prefix="/api/users", tags=["users"])
app.include_router(worlds_controller.router, prefix="/api/worlds", tags=["worlds"])
app.include_router(campaigns_controller.router, prefix="/api/campaigns", tags=["campaigns"])
app.include_router(mapRegions_controller.router, prefix="/api/regions", tags=["regions"])
app.include_router(sessions_controller.router, prefix="/api/sessions", tags=["sessions"])
app.include_router(markers_controller.router, prefix="/api/markers", tags=["markers"])
app.include_router(events_controller.router, prefix="/api/events", tags=["events"])
app.include_router(events_controller.router, prefix="/api/events", tags=["events"])
app.include_router(lore_controllers.router, prefix="/api/lore", tags=["lore"])



@app.get("/")
async def root():
    return {"message:" : "Root"}


