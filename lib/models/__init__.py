"""
Initialize the models package and make models available at the package level.
"""

# Import models so they are registered with Base.metadata
from .contact import Contact
from .communication import Communication

# Import Base and session from database to make them easily accessible
from ..database import Base, session, engine

# Define what gets imported with 'from lib.models import *'
__all__ = ['Contact', 'Communication']