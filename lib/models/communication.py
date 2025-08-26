# Day 1 task: imports, relationship, property methods.
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship
from lib.database import session, Base

class Communication(Base):
    __tablename__ = 'communications'

    id = Column(Integer, primary_key=True)
    contact_id = Column(Integer, ForeignKey('contacts.id'), nullable=False)
    date = Column(Date, nullable=False)
    notes = Column(String, nullable=False)

    # Many-to-one relationship: Communication belongs to a Contact
    contact = relationship('Contact', back_populates='communications')

    def __repr__(self):
        return f"<Communication(id={self.id}, contact_id={self.contact_id}, date={self.date}, notes='{self.notes[:30]}...')>"

    # --- Property Methods for Validation ---
    @property
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


    # Day 2 Task: ORM class methods
    @classmethod
    def create(cls, contact_id, date, notes):
        """Creates and saves a new Communication to the database."""
        communication = cls(contact_id=contact_id, date=date, notes=notes)
        session.add(communication)
        session.commit()
        return communication

    def delete(self):
        """Deletes this Communication from the database."""
        session.delete(self)
        session.commit()

    @classmethod
    def get_all(cls):
        """Retrieves all Communications from the database."""
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, id):
        """Finds a Communication by its ID."""
        return session.query(cls).filter_by(id=id).first()
