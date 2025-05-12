from fastapi import Request, Depends
from jose import jwt, JWTError
from starlette.status import HTTP_401_UNAUTHORIZED
from sqlalchemy.orm import Session
from app.core.exceptions import (
    ForbiddenActionError,
    MissingCredentialsError,
    UnauthorizedError,
)
from app.db.supabaseDB import get_db
from app.db.models import UserCampaignRole
import os

SUPABASE_JWT_SECRET = os.getenv("SUPABASE_JWT_SECRET")
SUPABASE_URL = os.getenv("SUPABASE_URL")

if not SUPABASE_JWT_SECRET:
    raise MissingCredentialsError()


def get_current_user_id(request: Request):
    token = request.headers.get("Authorization")

    if not token or not token.startswith("Bearer "):
        raise UnauthorizedError("No JWT provided")

    try:
        payload = jwt.decode(
            token[7:],
            SUPABASE_JWT_SECRET,
            algorithms=["HS256"],
            audience="authenticated",
            issuer=f"{SUPABASE_URL}/auth/v1",
        )
        return payload["sub"]  # Supabase puts UUID in `sub`

    except JWTError as e:
        raise UnauthorizedError(f"Invalid token: {e}")


def get_user_role_for_campaign(
    campaign_id: int, user_id: str, db: Session = Depends(get_db)
):
    role = (
        db.query(UserCampaignRole)
        .filter_by(user_id=user_id, campaign_id=campaign_id)
        .first()
    )

    if not role:
        raise ForbiddenActionError("You do not belong to this campaign.")

    return role.role


def require_role(campaign_id_param: str, allowed_roles: list[str]):
    def dependency(
        request: Request,
        db: Session = Depends(get_db),
        user_id: str = Depends(get_current_user_id),
    ):
        campaign_id = request.path_params.get(campaign_id_param)
        role = get_user_role_for_campaign(int(campaign_id), user_id, db)

        if role not in allowed_roles:
            raise ForbiddenActionError(f"Role: {role} is not allowed.")

        return {"user_id": user_id, "role": role}

    return dependency
