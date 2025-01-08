from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .config import settings
import urllib.parse

password = settings.dbPassword 
encoded_password = urllib.parse.quote_plus

DB_URL = f"postgresql://{settings}"

test = "plswork"