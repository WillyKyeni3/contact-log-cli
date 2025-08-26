# lib/debug.py
from lib.helpers import (
    create_contact, get_all_contacts, find_contact_by_id,
    create_communication, get_all_communications, find_communication_by_id,
    get_communications_for_contact
)
from lib.models import Contact, Communication

def test_contact_operations():
    print("\n=== TESTING CONTACT OPERATIONS ===")
    
    # Create a contact
    print("\n1. Creating a new contact...")
    contact = create_contact("Willy Musyoka", "willymusyoka@gmail.com", "0759 170970")
    print(f" Created contact: {contact}")
    
    # Get all contacts
    print("\n2. Getting all contacts...")
    all_contacts = get_all_contacts()
    print(f"Found {len(all_contacts)} contacts:")
    for c in all_contacts:
        print(f"  - {c}")
    
    # Find contact by ID
    print("\n3. Finding contact by ID...")
    found_contact = find_contact_by_id(contact.id)
    print(f"Found contact: {found_contact}")
    
    return contact

def test_communication_operations(contact):
    print("\n=== TESTING COMMUNICATION OPERATIONS ===")
    
    # Create a communication
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
    
    print("\n ALL TESTS COMPLETED SUCCESSFULLY!")

if __name__ == "__main__":
    main()