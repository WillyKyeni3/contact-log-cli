from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from lib.helpers import Base


class Communication(Base):
    __tablename__ = "communications"

    id = Column(Integer, primary_key=True)
    contact_id = Column(Integer, ForeignKey("contacts.id"), nullable=False)
    date = Column(Date, nullable=False)
    content = Column(String, nullable=False)

    # Relationship to the Contact model
    contact = relationship("Contact", back_populates="communications")

    def __repr__(self):
        return f"<Communication(id={self.id}, contact_id={self.contact_id}, date={self.date}, content={self.content})>"
    
    # Validation Property Methods 
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, (datetime.date, str)):
            raise ValueError("Date must be a date object or a string in YYYY-MM-DD format.")
        if isinstance(value, str):
            try:
                value = datetime.strptime(value, '%Y-%m-%d').date()
            except ValueError:
                raise ValueError("Date must be in YYYY-MM-DD format.")
        self._date = value
        
    @property
    def notes(self):
        return self._notes

    @notes.setter
    def notes(self, value):
        if not isinstance(value, str):
            raise ValueError("Notes must be a string.")
        if not value.strip():
            raise ValueError("Notes cannot be empty.")
        self._notes = value.strip()