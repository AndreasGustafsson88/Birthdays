from sqlalchemy.orm import relationship
from . import People
from db import Base
import sqlalchemy as db

from .Gifts import love_table


class Event(Base):
    __tablename__ = "events"

    EventId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.VARCHAR(100), nullable=False)
    Location = db.Column(db.VARCHAR(100), nullable=False)
    Description = db.Column(db.VARCHAR(255), nullable=True)
    Date = db.Column(db.DATE, nullable=False)
    people_id = db.Column(db.Integer, db.ForeignKey("people.PeopleId"))
    person = relationship(
        "People",
        back_populates="events"
    )
    gifts = relationship(
        "Gift",
        secondary=love_table,
        back_populates="Events"
    )

    def __repr__(self):
        return f"ID: {self.EventId} Name: {self.Name} Location: {self.Location} Description: {self.Description} Person: {self.person.FirstName} {self.person.LastName}" \
               f" Gift idea: {self.gifts}"