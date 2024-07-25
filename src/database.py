import sqlalchemy as sql

from .config import settings

engine = sql.create_engine(settings.database.url)
