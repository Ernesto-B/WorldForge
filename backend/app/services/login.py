from fastapi import HTTPException
from supabase import create_client
from dotenv import load_dotenv
import os

from app.core.exceptions import DatabaseQueryError, MissingCredentialsError, UnauthorizedError

load_dotenv()

def login_user(email:str, password: str):
    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY")

    if not SUPABASE_URL or not SUPABASE_KEY:
        raise MissingCredentialsError()

    try:
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

        response = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })

        if response.user is None:
            raise UnauthorizedError("Invalid email or password.")

        return response

    except UnauthorizedError:
        raise
    except Exception as e:
        raise DatabaseQueryError(f"Failed to login: {e}")
