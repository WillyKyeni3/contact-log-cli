# Import models to register with Base.metadata
from .contact import Contact
from .communicaton import Communication

# import Base and session from helpers for easier access
from ..helpers import Base, session, engine

# Definition of what is imported with " from lib.models import"
__all__ = ['Contact', 'Communication']