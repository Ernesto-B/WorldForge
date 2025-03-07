from fastapi import FastAPI

app = FastAPI()

app.include_router(auth_controller.router, prefix="/api/auth", tags=["auth"])



@app.get("/")
async def root():
    return {"message:" : "Root"}

