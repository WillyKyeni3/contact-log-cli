# Day 1 tasks 
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from lib.helpers import session, Base

class Contact(Base):
    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String)
    phone_number = Column(String)

    # One-to-many relationship, Contact has many Communications
    communications = relationship('Communication', back_populates='contact', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Contact(id={self.id}, name='{self.name}', email='{self.email}', phone='{self.phone_number}')>"

    # Property Methods for Validation 
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        if not value.strip():
            raise ValueError("Name cannot be empty or whitespace.")
        self._name = value.strip()

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if value is not None and not isinstance(value, str):
            raise ValueError("Email must be a string or None.")
        if value and '@' not in value:
            raise ValueError("Invalid email format.")
        self._email = value

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        if value is not None and not isinstance(value, str):
            raise ValueError("Phone number must be a string or None.")
        self._phone_number = value
        
        
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
