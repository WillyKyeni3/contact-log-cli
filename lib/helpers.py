from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import event
from sqlalchemy.engine import Engine
import os
import sqlite3
from lib.models.communication import Communication
from lib.models.contact import Contact

# Enables foreign key constraints for SQLite
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, sqlite3.Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()

# Use SQLite for simplicity
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
    print("Database & tables created successfully.")

def close_db():
    """Close the database session."""
    session.close()


# Day 2 task: Utility functions
# contact
def create_contact(name, email=None, phone_number=None):
    """Helper to create a contact through the models's create method."""
    return Contact.create(name, email, phone_number)

def get_all_contact():
    """Helper to retrieve all contacts."""
    return Contact.get_all()

def find_contact_by_id(id):
    """Helper to find a contact by ID."""
    return Contact.find_by_id(id)

# communication
def create_communication(contact_id, date, notes):
    """Helper to create a communication through the model's create method."""
    return Communication.create(contact_id, date, notes)

def get_all_communications():
    """Helper to get all communications."""
    return Communication.get_all()

def find_communication_by_id(id):
    """Helper to find a communication by ID."""
    return Communication.find_by_id(id)

def get_communications_for_contact(contact_id):
    """Get all communications for a specific contact."""
    contact = find_contact_by_id(contact_id)
    if contact:
        return contact.get_communications()
    return None