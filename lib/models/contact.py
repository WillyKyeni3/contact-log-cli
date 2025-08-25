from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from lib.helpers import session, Base


class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String)
    phone_number = Column(String)
    
    # One-to-many relationship: Contact has many Communications
    communications = relationship('Communication', back_populates='contact', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Contact(id={self.id}, name={self.name}, email={self.email}, phone_number={self.phone_number})>"
    
    # Property methods for validation
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if len(value.strip()) == 0:
            raise ValueError("Name cannot be empty")
        self._name = value.strip()
        
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        # Simple email validation
        if value is not None and not isinstance(value, str):
            raise ValueError("Email must be a string or None")
        if value and '@' not in value:
            raise ValueError("Invalid email format")
        self._email = value