from dependency.di_container import container
from fastapi import Request, Response
from supabase import Client, ClientOptions, create_client


def base_supabase(api_key: str) -> Client:
    settings = container.app_settings()
    return create_client(
        settings.supabase_config.url,
        api_key,
        options=ClientOptions(auto_refresh_token=False, persist_session=False),
    )


async def supabase_auth_middleware(request: Request, call_next):
    settings = container.app_settings()
    jwt = None
    auth = request.headers.get("Authorization", "")
    if auth.startswith("Bearer "):
        jwt = auth.removeprefix("Bearer ").strip()
    else:
        jwt = request.cookies.get(settings.supabase_config.jwt_cokie_name)

    request.state.user = None
    request.state.jwt = None
    if jwt:
        sb_client: Client = base_supabase(settings.supabase_config.anon_key)
        try:
            claims_res = sb_client.auth.get_user(jwt)
            if claims_res and claims_res.user:
                request.state.user = {
                    "id": claims_res.user.id,
                    "claims": claims_res.user,
                }
                request.state.jwt = jwt
            else:
                user_res = sb_client.auth.get_user(jwt)
                if user_res and user_res.user and user_res.user.id:
                    request.state.user = {
                        "id": user_res.user.id,
                        "claims": user_res.user,
                    }
                    request.state.jwt = jwt
        except Exception:
            pass

    response: Response = await call_next(request)
    return response
