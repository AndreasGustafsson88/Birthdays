import sqlalchemy as db

from sqlalchemy.orm import relationship
from Data.Models.Love_Tables import love_table
from Data.db import Base


class Gift(Base):
    __tablename__ = "gifts"

    GiftId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.VARCHAR(100), nullable=False)
    Price = db.Column(db.Integer, nullable=False)
    Link = db.Column(db.VARCHAR(255), nullable=True)
    Events = relationship(
        "Event",
        secondary=love_table,
        back_populates="gifts"
    )

    def __repr__(self):
        return f"ID: {self.GiftId} Name: {self.Name} Price: {self.Price} Link: {self.Link}"