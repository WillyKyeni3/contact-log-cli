from lib.helpers import (
    create_contact, get_all_contact, find_contact_by_id,
    create_communication, get_all_communications, find_communication_by_id,
    get_communications_for_contact
)
from datetime import datetime, date
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
        
def view_contact_details():
    """Displays details of a specific contact by ID."""
    try:
        contact_id = int(input("\nEnter contact ID: "))
        contact = find_contact_by_id(contact_id)
        
        if not contact:
            print(f"\n❌ Contact with ID {contact_id} not found.")
            return
        display_contact(contact)
        
    # show communications for this conatact
        communications = get_communications_for_contact(contact_id)
        if communications:
            print("\nCommunications:")
            for comm in communications:
                print(f"- {comm.date}: {comm.notes[:50]}{'...' if len(comm.notes) > 50 else ''}")
        else:
            print("\nNo communications found for this contact.")
            
    except ValueError:
        print("\n❌ Invalid ID format. Please enter a number.")
        
def delete_contact():
    """Delete a contact after confirmation."""
    try:
        contact_id = int(input("\nEnter contact ID to delete: "))
        contact = find_contact_by_id(contact_id)
        
        if not contact:
            print(f"\n❌ Contact with ID {contact_id} not found.")
            return
            
        # Confirm deletion
        print("\nAre you sure you want to delete this contact?")
        display_contact(contact)
        
        confirm = input("\nType 'yes' to confirm deletion: ").strip().lower()
        if confirm == 'yes':
            contact.delete()
            print(f"\n✅ Contact '{contact.name}' deleted successfully.")
        else:
            print("\n❌ Deletion cancelled.")
            
    except ValueError:
        print("\n❌ Invalid ID format. Please enter a number.")

        
# Communication
def list_all_communications():
    """Display all communications in a user-friendly format."""
    comms = get_all_communications()
    if not comms:
        print("\nNo communications found.")
        return
    
    print("\nAll Communications:")
    for comm in comms:
        contact = find_contact_by_id(comm.contact_id)
        contact_name = contact.name if contact else "[Unknown Contact]"
        print(f"- ID: {comm.id} | {contact_name} | {comm.date}: {comm.notes[:50]}{'...' if len(comm.notes) > 50 else ''}")
        

def create_new_communication():
    """Create a new communication entry for a contact."""
    try:
        contact_id = int(input("\nEnter contact ID: "))
        contact = find_contact_by_id(contact_id)
        
        if not contact:
            print(f"\n❌ Contact with ID {contact_id} not found.")
            return
            
        print(f"\nCreating communication for: {contact.name}")
        
        # Get date with validation
        while True:
            date_str = input("Enter date (YYYY-MM-DD): ").strip()
            try:
                # validate the format
                datetime.strptime(date_str, '%Y-%m-%d') 
                break
            except ValueError:
                print("❌ Invalid date format. Please use YYYY-MM-DD.")
        
        notes = input("Enter communication notes: ").strip()
        if not notes:
            print("\n❌ Notes cannot be empty.")
            return
            
        comm = create_communication(contact_id, date_str, notes)
        print(f"\n✅ Communication created successfully! ID: {comm.id}")
        display_communication(comm)
        
    except ValueError:
        print("\n❌ Invalid ID format. Please enter a number.")
        
        
def view_communications_for_contact():
    """Display all communications for a specific contact."""
    try:
        contact_id = int(input("\nEnter contact ID: "))
        contact = find_contact_by_id(contact_id)
        
        if not contact:
            print(f"\n❌ Contact with ID {contact_id} not found.")
            return
            
        print(f"\nCommunications for {contact.name}:")
        communications = get_communications_for_contact(contact_id)
        
        if not communications:
            print("No communications logged for this contact.")
            return
            
        for comm in communications:
            print(f"\n- ID: {comm.id}")
            print(f"  Date: {comm.date}")
            print(f"  Notes: {comm.notes}")
            
    except ValueError:
        print("\n❌ Invalid ID format. Please enter a number.")
        
        
def delete_communication():
    """Delete a communication entry after confirmation."""
    try:
        comm_id = int(input("\nEnter communication ID to delete: "))
        comm = find_communication_by_id(comm_id)
        
        if not comm:
            print(f"\n❌ Communication with ID {comm_id} not found.")
            return
            
        # Get associated contact
        contact = find_contact_by_id(comm.contact_id)
        contact_name = contact.name if contact else "[Unknown Contact]"
        
        print(f"\nAre you sure you want to delete this communication?")
        print(f"From: {contact_name}")
        print(f"Date: {comm.date}")
        print(f"Notes: {comm.notes}")
        
        confirm = input("\nType 'yes' to confirm deletion: ").strip().lower()
        if confirm == 'yes':
            comm.delete()
            print("\n✅ Communication deleted successfully.")
        else:
            print("\n❌ Deletion cancelled.")
            
    except ValueError:
        print("\n❌ Invalid ID format. Please enter a number.")


def main():
    print("===== WELCOME TO CONTACT-LOG CLI =====")
    print("Your professional relationship tracker")
    
    while True:
        menu()
        choice = input("Select an option: ").strip()
        
        if choice == "0":
            print("\nGoodbye! Thanks for using Contact-Log CLI.")
            break
            
        elif choice == "1":
            # Contact management submenu
            while True:
                contact_menu()
                contact_choice = input("Select an option: ").strip()
                
                if contact_choice == "0":
                    break
                elif contact_choice == "1":
                    list_all_contacts()
                elif contact_choice == "2":
                    create_new_contact()
                elif contact_choice == "3":
                    view_contact_details()
                elif contact_choice == "4":
                    delete_contact()
                else:
                    print("\n❌ Invalid option. Please try again.")
                    
        elif choice == "2":
            # Communication management submenu
            while True:
                communication_menu()
                comm_choice = input("Select an option: ").strip()
                
                if comm_choice == "0":
                    break
                elif comm_choice == "1":
                    list_all_communications()
                elif comm_choice == "2":
                    create_new_communication()
                elif comm_choice == "3":
                    view_communications_for_contact()
                elif comm_choice == "4":
                    delete_communication()
                else:
                    print("\n❌ Invalid option. Please try again.")
                    
        else:
            print("\n❌ Invalid option. Please try again.")

if __name__ == "__main__":
    main()