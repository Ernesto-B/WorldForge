from fastapi import HTTPException
from supabase import create_client
from dotenv import load_dotenv
import os

from app.core.exceptions import DatabaseQueryError, DatabaseSaveError, UnauthorizedError

load_dotenv()

def register_user(email: str, password: str):
    if len(password) < 6:
        raise HTTPException(400, "Password must be at least 6 characters.")

    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY")

    if not SUPABASE_URL or not SUPABASE_KEY:
        raise DatabaseQueryError("Supabase credentials missing.")

    try:
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        response = supabase.auth.sign_up({
            "email": email,
            "password": password
        })

        if response.user is None:
            raise UnauthorizedError("Invalid email or password.")

        return response

    except Exception as e:
        raise DatabaseSaveError(f"Failed to register {e}")

