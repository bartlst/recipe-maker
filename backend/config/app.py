from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, Field

class SupabaseSettings(BaseSettings):
    url: str = ""
    key: str = ""

    model_config = SettingsConfigDict(env_prefix="SUPABASE_")


class AppSettings(BaseModel):
    supabase_config: SupabaseSettings = Field(default_factory=SupabaseSettings)