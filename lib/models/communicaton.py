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