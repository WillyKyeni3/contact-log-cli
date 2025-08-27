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
    
def list_all_contacts():
    """Display all contacts in a user-friendly format."""
    contacts = get_all_contact()
    if not contacts:
        print("\nNo contacts found.")
        return
    print("\nAll Contacts:")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact.name} (ID: {contact.id})")
        
def create_new_contact():
    """Prompt user for contact details and create a new contact."""
    print("\n--- Create New Contact ---")
    
    name = input("Enter contact name: ").strip()
    if not name:
        print("Error: Name cannot be empty.")
        return
    
    email = input("Enter email (optional): ").strip() or None
    phone = input("Enter phone number (optional): ").strip() or None
    
    try:
        contact = create_contact(name, email, phone)
        print(f"\n✅ Contact created successfully! ID: {contact.id}")
        display_contact(contact)
    except ValueError as e:
        print(f"\n❌ Error creating contact: {str(e)}")