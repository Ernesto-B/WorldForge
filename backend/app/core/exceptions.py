from fastapi import HTTPException, status

# Use whenever you want to raise the 404 exception in a service
# def safe_query_or_404(query_result, message="Resource not found."):
#     if not query_result:
#         raise HTTPException(status_code=404, detail=message)
#     return query_result

class UserNotFoundError(HTTPException):
    def __init__(self, detail: str = "Resource not found."):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)

class UnauthorizedError(HTTPException):
    def __init__(self, detail: str = "Not authorized."):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail=detail)

class BadRequestError(HTTPException):
    def __init__(self, detail: str = "Bad request (invalid input, missing fields, bad data)."):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)

class InvalidJoinCodeError(HTTPException):
    def __init__(self, detail: str = "Invalid join code (invalid input, missing fields, bad data)."):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)

class CampaignNotFoundError(HTTPException):
    def __init__(self, detail: str = "Campaign not found."):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)

class WorldNotFoundError(HTTPException):
    def __init__(self, detail: str = "World not found."):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)

# Use this one if SUPABASE KEY or URL are missing
class DatabaseQueryError(HTTPException):
    def __init__(self, detail: str = "Database query error (selects, queries)."):
        super().__init__(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=detail)

class DatabaseSaveError(HTTPException):
    def __init__(self, detail: str = "Database save error (insert, update, delete)."):
        super().__init__(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=detail)
        
class MissingCredentialsError(HTTPException):
    def __init__(self, detail: str = "Credentials missing."):
        super().__init__(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=detail)

# Use this when roles are not sufficient
class ForbiddenActionError(HTTPException):
    def __init__(self, detail: str = "User is authenticated but not authorized."):
        super().__init__(status_code=status.HTTP_403_FORBIDDEN, detail=detail)

