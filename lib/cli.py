from lib.helpers import (
    create_contact, get_all_contact, find_contact_by_id,
    create_communication, get_all_communications, find_communication_by_id,
    get_communications_for_contact
)
from lib.models import Contact, Communication

# Display the menu options
def menu():
    """Main meni options display."""
    print("\n===== CONTACT-LOG =====")
    print("1. Manage Contacts")
    print("2. Manage Communications")
    print("0. Exit the application")
    print("===========================")
    
def contact_menu():
    """Display the contact management menu."""
    print("\n===== CONTACT MANAGEMENT =====")
    print("1. List all contacts")
    print("2. Create a new contact")
    print("3. View a contact's details")
    print("4. Delete a contact")
    print("0. Back to main menu")