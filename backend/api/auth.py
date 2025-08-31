from fastapi import Depends
from fastapi.routing import APIRouter
from dependency.di_container import container
from fastapi.security import OAuth2PasswordBearer
from supabase_auth.errors import AuthApiError

from supabase_auth.types import SignInWithEmailAndPasswordCredentials


auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.post("/login")
async def login(
    email: str,
    password: str,
):
    pass

@auth_router.post("/register")
async def register(
    email: str,
    password: str,
):
    try:
        user = container.supabase_client().auth.sign_up({"email": email, "password": password})
        return {"message": "User registered successfully", "user": user}
    except Exception as e:
        return {"error": str(e)}

@auth_router.post("/logout")
async def logout(
):
    pass


@auth_router.get("/me")
async def get_current_user():
    pass