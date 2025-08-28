from lib.database import session, Base, engine
from lib.models import Contact, Communication
from datetime import date, datetime


# Utility functions
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

def search_contacts(name):
    """Helper to search contacts by name."""
    return Contact.find_by_name(name)

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


def validate_date(date_string):
    """Validate date string is in YYYY-MM-DD format."""
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def get_valid_date(prompt):
    """Prompt user for a valid date with retries."""
    while True:
        date_str = input(prompt).strip()
        if validate_date(date_str):
            return date_str
        print("❌ Invalid date format. Please use YYYY-MM-DD.")

def get_non_empty_input(prompt, error_msg="Cannot be empty."):
    """Get non-empty input from user with validation."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print(f"❌ {error_msg}")