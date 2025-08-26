from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import events
from sqlalchemy.engine import Engine
import os
import sqlite3

# Enable foreign key support for SQLite
@events.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, sqlite3.Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()
        
# Define the SQLite database file path
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///contact_log.db')

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)

# sessionmaker factory
Session = sessionmaker(bind=engine)
session = Session()