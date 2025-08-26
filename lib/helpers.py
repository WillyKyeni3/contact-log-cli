# lib/helpers.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import event
from sqlalchemy.engine import Engine
import os
import sqlite3

# Enable foreign key constraints for SQLite
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, sqlite3.Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()

# Use SQLite for simplicity (you can change to MySQL later if needed)
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///contact_log.db')

# Create engine
engine = create_engine(DATABASE_URL, echo=True)

# Create session factory
Session = sessionmaker(bind=engine)
session = Session()

# Base class for models
Base = declarative_base()

def init_db():
    """Create all tables in the database."""
    Base.metadata.create_all(engine)
    print("✅ Database & tables created successfully.")

def close_db():
    """Close the database session."""
    session.close()