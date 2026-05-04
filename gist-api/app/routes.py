from fastapi import APIRouter, HTTPException
from app.services import fetch_gists

router = APIRouter()

@router.get("/{username}")
def get_user_gists(username: str):
    try:
        return fetch_gists(/users/{username}/gists)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")