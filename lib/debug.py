# lib/debug.py
from lib.helpers import (
    create_contact, get_all_contact, find_contact_by_id,
    create_communication, get_all_communications, find_communication_by_id,
    get_communications_for_contact
)
from lib.models import Contact, Communication

def test_contact_operations():
    print("\n=== TESTING CONTACT OPERATIONS ===")
    
    # Creates a contact
    print("\n1. Creating a new contact...")
    contact = create_contact("Willy Musyoka", "willymusyoka@gmail.com", "0759 170970")
    print(f" Created contact: {contact}")
    
    # Get all contacts
    print("\n2. Getting all contacts...")
    all_contacts = get_all_contact()
    print(f"Found {len(all_contacts)} contacts:")
    for c in all_contacts:
        print(f"  - {c}")
    
    # Finds contact by ID
    print("\n3. Finding contact by ID...")
    found_contact = find_contact_by_id(contact.id)
    print(f"Found contact: {found_contact}")
    
    return contact

def test_communication_operations(contact):
    print("\n=== TESTING COMMUNICATION OPERATIONS ===")

    # Creates a communication
    print("\n1. Creating a communication for the contact...")
    comm = create_communication(
        contact.id,
        "2025-08-26",
        "Discussed project timeline and Tasks to be done"
    )
    print(f" Created communication: {comm}")
    
    # Get all communications
    print("\n2. Getting all communications...")
    all_comms = get_all_communications()
    print(f"Found {len(all_comms)} communications:")
    for c in all_comms:
        print(f"  - {c}")
    
    # Find communication by ID
    print("\n3. Finding communication by ID...")
    found_comm = find_communication_by_id(comm.id)
    print(f"Found communication: {found_comm}")
    
    # Get communications for contact
    print("\n4. Getting all communications for the contact...")
    contact_comms = get_communications_for_contact(contact.id)
    print(f"Found {len(contact_comms)} communications for contact:")
    for c in contact_comms:
        print(f"  - {c}")
    
    return comm

def test_relationships(contact, comm):
    print("\n=== TESTING RELATIONSHIPS ===")
    
    # Test the relationship from contact to communications
    print("\n1. Testing contact.communications...")
    print(f"Contact {contact.name} has {len(contact.communications)} communications:")
    for c in contact.communications:
        print(f"  - {c}")
    
    # Test the relationship from communication to contact
    print("\n2. Testing communication.contact...")
    print(f"Communication belongs to contact: {comm.contact.name}")

def test_deletion(contact, comm):
    print("\n=== TESTING DELETION ===")
    
    # Delete the communication
    print("\n1. Deleting the communication...")
    comm.delete()
    print(" Communication deleted")
    
    # Verify it's gone
    deleted_comm = find_communication_by_id(comm.id)
    print(f"Communication still exists? {'Yes' if deleted_comm else 'No'}")
    
    # Recreate for contact deletion test
    comm = create_communication(
        contact.id,
        "2024-08-26",
        "Follow-up meeting about project"
    )
    
    # Delete the contact (should delete communications too due to cascade)
    print("\n2. Deleting the contact (and its communications)...")
    contact.delete()
    print(" Contact deleted")
    
    # Verify contact is gone
    deleted_contact = find_contact_by_id(contact.id)
    print(f"Contact still exists? {'Yes' if deleted_contact else 'No'}")
    
    # Verify communications are gone
    communications_after_delete = get_communications_for_contact(contact.id)
    print(f"Communications still exist? {'Yes' if communications_after_delete else 'No'}")

# CLI flow tests
def test_cli_flow():
    """Test a complete CLI interaction flow."""
    print("\n=== TESTING CLI FLOW ===")
    
    # Create test data
    contact = create_contact("CLI Test Contact", "cli@test.com", "555-0100")
    print(f"Created test contact: {contact}")
    
    # Create communications
    create_communication(contact.id, "2024-08-25", "Initial meeting about CLI testing")
    create_communication(contact.id, "2024-08-26", "Follow-up on CLI functionality")
    print("Created test communications")
    
    # Test contact operations
    print("\n1. Testing contact listing...")
    list_all_contacts()
    
    print("\n2. Testing contact details...")
    view_contact_details_for(contact.id)
    
    # Test communication operations
    print("\n3. Testing communication listing...")
    list_all_communications()
    
    print("\n4. Testing communications for contact...")
    view_communications_for_contact(contact.id)
    
    # Cleanup
    print("\n5. Cleaning up test data...")
    contact.delete()
    print(" Test data cleaned up")

# helper functions for the CLI tests
def list_all_contacts():
    """CLI-style contact listing."""
    contacts = get_all_contact()
    if not contacts:
        print("No contacts found.")
        return
    
    print("All Contacts:")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact.name} (ID: {contact.id})")

def view_contact_details_for(contact_id):
    """CLI-style contact details display."""
    contact = find_contact_by_id(contact_id)
    if not contact:
        print(f"Contact with ID {contact_id} not found.")
        return
    
    print(f"\nContact ID: {contact.id}")
    print(f"Name: {contact.name}")
    print(f"Email: {contact.email or 'N/A'}")
    print(f"Phone: {contact.phone_number or 'N/A'}")
    
    communications = get_communications_for_contact(contact_id)
    if communications:
        print("\nRecent Communications:")
        for comm in communications:
            print(f"- {comm.date}: {comm.notes[:50]}{'...' if len(comm.notes) > 50 else ''}")

def list_all_communications():
    """CLI-style communication listing."""
    comms = get_all_communications()
    if not comms:
        print("No communications found.")
        return
    
    print("All Communications:")
    for comm in comms:
        contact = find_contact_by_id(comm.contact_id)
        contact_name = contact.name if contact else "[Unknown Contact]"
        print(f"- ID: {comm.id} | {contact_name} | {comm.date}: {comm.notes[:50]}{'...' if len(comm.notes) > 50 else ''}")

def view_communications_for_contact(contact_id):
    """CLI-style communications display for a contact."""
    contact = find_contact_by_id(contact_id)
    if not contact:
        print(f"Contact with ID {contact_id} not found.")
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
        
        
def main():
    print(" Setting up the Contact-Log database...")
    
    # resets (deletes all tables & recreates them) the database for clean testing
    from lib.helpers import Base, engine
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    
    # Run tests
    contact = test_contact_operations()
    comm = test_communication_operations(contact)
    test_relationships(contact, comm)
    test_deletion(contact, comm)
    test_cli_flow()
    
    print("\n ALL TESTS COMPLETED SUCCESSFULLY!")

if __name__ == "__main__":
    main()