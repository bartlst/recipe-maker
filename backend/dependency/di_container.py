from dependency_injector import containers, providers
from supabase import create_client
from config.app import AppSettings

class Container(containers.DeclarativeContainer):

    app_settings = providers.Singleton(AppSettings)
    print(app_settings().supabase_config)
    
    #TODO: make client setup with lambda to handle overrides for testing
    supabase_client = providers.Singleton(
        create_client,
        supabase_url=app_settings().supabase_config.url,
        supabase_key=app_settings().supabase_config.key
    )


container = Container()