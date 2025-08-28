# Day 1 tasks 
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.orm import validates
from lib.database import session, Base

class Contact(Base):
    __tablename__ = 'contacts'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String)
    phone_number = Column(String)
    
    communications = relationship('Communication', back_populates='contact', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f"<Contact(id={self.id}, name='{self.name}', email='{self.email}', phone='{self.phone_number}')>"
    
    
    @validates('name')
    def validate_name(self, key, value):
        """Validate name when setting the name attribute."""
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        if not value.strip():
            raise ValueError("Name cannot be empty or whitespace.")
        return value.strip()
    
    @validates('email')
    def validate_email(self, key, value):
        """Validate email when setting the email attribute."""
        if value is not None and not isinstance(value, str):
            raise ValueError("Email must be a string or None.")
        if value and '@' not in value:
            raise ValueError("Invalid email format.")
        return value
    
    @validates('phone_number')
    def validate_phone_number(self, key, value):
        """Validate phone number when setting the phone_number attribute."""
        if value is not None and not isinstance(value, str):
            raise ValueError("Phone number must be a string or None.")
        return value
        
        
    # Day 2 Task: ORM class methods
    @classmethod
    def create(cls, name, email=None, phone_number=None):
        """Creates and saves a new Contact to the database."""
        contact = cls(name=name, email=email, phone_number=phone_number)
        session.add(contact)
        session.commit()
        return contact
    
    def delete(self):
        """Delete this Contact from the database."""
        session.delete(self)
        session.commit()
        
    @classmethod
    def get_all(cls):
        """Retrieves all Contacts from the database."""
        return session.query(cls).all()
    
    @classmethod
    def find_by_id(cls, id):
        """Finds a Contact by its ID."""
        return session.query(cls).filter_by(id=id).first()

    def get_communications(self):
        """Returns all Communications for this Contact."""
        return self.communications
    
    @classmethod
    def find_by_name(cls, name):
        """Finds contacts by name (case-insensitive)."""
        return session.query(cls).filter(cls.name.ilike(f'%{name}%')).all()
