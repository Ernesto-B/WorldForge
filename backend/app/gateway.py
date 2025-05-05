from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError
from app.controllers.auth_controller import auth_controller
from app.controllers.world_controller import world_controller
from app.controllers.users_controller import users_controller
# from app.controllers.campaign_controller import campaigns_controller

app = FastAPI()

# ONLY FOR PRODUCTION
# # Handler for SQLAlchemy "DB" errors
# @app.exception_handler(SQLAlchemyError)
# async def sqlalchemy_exception_handler(request: Request, exc: SQLAlchemyError):
#     print(f"Database error: {exc}")
#     return JSONResponse(
#         status_code=400,
#         content={"detail":"A database error occured."}
#     )
#
# # Handler for bad client inputs
# @app.exception_handler(RequestValidationError)
# async def sqlalchemy_exception_handler(request: Request, exc: RequestValidationError):
#     print(f"Validation error: {exc}")
#     return JSONResponse(
#         status_code=422,
#         content={"detail": exc.errors()}
#     )
#
# # Generic catch-all fallback if all else fails
# @app.exception_handler(Exception)
# async def generic_exception_handler(request: Request, exc: Exception):
#     print(f"Unexpected error: {exc}")
#     return JSONResponse(
#         status_code=500,
#         content={"detail":"Internal server error"}
#     )

# core routers
app.include_router(auth_controller, prefix="/api/auth", tags=["auth"])
app.include_router(users_controller, prefix="/api/users", tags=["users"])
app.include_router(world_controller, prefix="/api/worlds", tags=["worlds"])

# # campaigns
# app.include_router(campaigns_controller, prefix="/api/campaigns", tags=["campaigns"])
# app.include_router(campaigns_controller.router, prefix="/api/worlds/{world_id}/campaigns", tags=["campaigns"])

# # regions
# app.include_router(mapRegions_controller.router, prefix="/api/regions", tags=["regions"])
# app.include_router(mapRegions_controller.router, prefix="/api/worlds/{world_id}/regions", tags=["regions"])


# app.include_router(sessions_controller.router, prefix="/api/sessions", tags=["sessions"])
# app.include_router(sessions_controller.router, prefix="/api/campaigns/{campaign_id}/sessions", tags=["sessions"])

# # markers
# app.include_router(markers_controller.router, prefix="/api/markers", tags=["markers"])
# app.include_router(markers_controller.router, prefix="/api/worlds/{world_id}/markers", tags=["markers"])

# # world events
# app.include_router(events_controller.router, prefix="/api/events", tags=["events"])
# app.include_router(events_controller.router, prefix="/api/worlds/{world_id}/events", tags=["events"])

# # lore entries
# app.include_router(lore_controller.router, prefix="/api/lore", tags=["lore"])
# app.include_router(lore_controller.router, prefix="/api/regions/{region_id}/lore", tags=["lore"])


@app.get("/")
async def root():
    return {"message:" : "Root"}
