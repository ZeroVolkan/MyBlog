from pydantic_settings import BaseSettings, SettingsConfigDict

class SettingsDB(BaseSettings):
    host_db: str
    port_db: int
    user_db: str
    password_db: str
    name_db: str
    driver_db: str = "psycopg2"

    @property
    def url(self):
        return f"postgresql+{self.driver_db}://{self.user_db}:{self.password_db}@{self.host_db}:{self.port_db}/{self.name_db}"

    model_config = SettingsConfigDict(env_file=".env")


class Settings(BaseSettings):
    name_project: str = "MyBlog"
    database: SettingsDB = SettingsDB()



settings = Settings()
