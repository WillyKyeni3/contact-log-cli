from lib.database import session, Base, engine
from lib.models import Contact, Communication


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