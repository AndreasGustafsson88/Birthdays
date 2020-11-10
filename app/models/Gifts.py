from sqlalchemy.orm import relationship

from db import Base
import sqlalchemy as db


love_table = db.Table(
    "association",
    Base.metadata,
    db.Column("left_id", db.Integer, db.ForeignKey("left.id")),
    db.Column("left_id", db.Integer, db.ForeignKey("left.id"))
)


class Gift(Base):
    __tablename__ = "gifts"

    GiftId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.VARCHAR(100), nullable=False)
    Price = db.Column(db.Integer, nullable=False)
    Link = db.Column(db.VARCHAR(255), nullable=True)
    children = relationship(
        "events",
        secondary=love_table
    )

    def __repr__(self):
        return f"ID: {self.PeopleId} Name: {self.FirstName} {self.LastName} DOB: {self.DOB} Relation: {self.Relation}"