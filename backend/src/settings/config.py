from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    CMC_API_KEY: str
    JWT_SECRET_KEY: str
    BASE_URL: str
    DATA_BASE_URL_FIREBASE: str
    STORAGE_BUCKET: str
    URL_CLOUD_STORAGE: str

    @property
    def DATABASE_URL_asyncpg(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    @property
    def DATABASE_URL_psycopg(self):
        return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()

# Settings -> file marketplace/backend/.env
#The struct of file .env
#DB_HOST=localhost
#DB_PORT=5432
#DB_USER=postgres
#DB_PASS=root
#DB_NAME=market
#CMC_API_KEY= https://coinmarketcap.com/api/
#JWT_SECRET_KEY= https://jwt.io/