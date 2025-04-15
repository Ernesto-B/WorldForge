from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()


def register_user(email: str, password: str):
    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY")

    if not SUPABASE_URL or not SUPABASE_KEY:
        return

    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

    response = supabase.auth.sign_up({
        "email": email,
        "password": password
    })
    return response
