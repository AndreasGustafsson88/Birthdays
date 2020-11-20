import sqlalchemy as db
from Data.db import Base


love_table = db.Table(
    "association",
    Base.metadata,
    db.Column("event_id", db.Integer, db.ForeignKey("events.EventId")),
    db.Column("gift_id", db.Integer, db.ForeignKey("gifts.GiftId"))
)