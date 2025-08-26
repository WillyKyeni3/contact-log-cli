# lib/debug.py
from lib.helpers import init_db, session, Base, engine
from lib.models import Contact, Communication

def main():
    print(" Setting up the Contact-Log database...")
    init_db()

    # Optional: Print table names to confirm
    print(" Tables in database:")
    for table in Base.metadata.tables:
        print(f"  - {table}")

if __name__ == "__main__":
    main()