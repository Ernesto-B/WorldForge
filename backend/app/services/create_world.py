from fastapi import HTTPException
from supabase import create_client
from dotenv import load_dotenv
from pydantic_extra_types.pendulum_dt import Date
import os

load_dotenv()

def create_world(id:str, name: str, description: str, created_at: Date):
    if len(description) > 100:
        raise HTTPException(400, "Description is over the 100 character limit.")
    
    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY")

    if not SUPABASE_URL or not SUPABASE_KEY:
        raise HTTPException(500, "Supabase credentials missing")
    
    try:
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

        response = "Add db stuff when Ernesto is done"

        return response
    
    except Exception as e: 
        raise HTTPException(500, str(e))