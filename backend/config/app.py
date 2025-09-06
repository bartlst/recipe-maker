from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class SupabaseSettings(BaseSettings):
    url: str = ""
    anon_key: str = ""
    service_role_key: str = ""
    jwt_cokie_name: str = "sb-jwt"
    refresh_cookie_name: str = "sb-refresh-token"

    model_config = SettingsConfigDict(env_prefix="SUPABASE_")


class AppSettings(BaseModel):
    supabase_config: SupabaseSettings = Field(default_factory=SupabaseSettings)
