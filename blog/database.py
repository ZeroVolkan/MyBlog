from pydantic import BaseModel
from config import config

import sqlalchemy as sql

name     = config['database']['name']
password = config['database']['password']
host     = config['database']['host']
database = config['database']['database']

engine = sql.create_engine('mysql+')