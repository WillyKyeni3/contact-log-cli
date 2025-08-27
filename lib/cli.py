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
    """Display the contact management submenu."""
    print("\n--- CONTACT MANAGEMENT ---")
    print("1. List all contacts")
    print("2. Create a new contact")
    print("3. View a contact's details")
    print("4. Delete a contact")
    print("0. Back to main menu")
    print("------------------------")
    
def communication_menu():
    """Display the communication management submenu."""
    print("\n--- COMMUNICATION MANAGEMENT ---")
    print("1. List all communications")
    print("2. Create a new communication")
    print("3. View communication for a contact")
    print("4. Delete a communication")
    print("0. Back to main menu")
    print("------------------------")
    
def display_contact(contact):
    """Format and display a contact's information."""
    print(f"\nContact ID: {contact.id}")
    print(f"Name: {contact.name}")
    print(f"Email: {contact.email or 'N/A'}")
    print(f"Phone: {contact.phone_number or 'N/A'}")
    
def display_communication(comm):
    """Format and display a communication's information."""
    print(f"\nCommunication ID: {comm.id}")
    print(f"Date: {comm.date}")
    print(f"Notes: {comm.notes}")