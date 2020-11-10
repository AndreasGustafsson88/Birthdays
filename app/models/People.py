from sqlalchemy.orm import relationship

from db import Base
import sqlalchemy as db


class People(Base):
    __tablename__ = "people"

    PeopleId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    FirstName = db.Column(db.VARCHAR(45), nullable=False)
    LastName = db.Column(db.VARCHAR(45), nullable=False)
    DOB = db.Column(db.DATE, nullable=False)
    Relation = db.Column(db.VARCHAR(45), nullable=False)
    events = relationship("Event", back_populates="person")

    def __repr__(self):
        return f"ID: {self.PeopleId} Name: {self.FirstName} {self.LastName} DOB: {self.DOB} Relation: {self.Relation} Future Events: {''.join(event.Name + ' on ' +  str(event.Date) for event in self.events)}"