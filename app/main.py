from Data.db import session, Base, engine
from Data.Models.Events import Event
from Data.Models.Gifts import Gift
from Data.Models.People import People
from UI.main_menu import main_menu





def add_event(name, location, description, date, person_id):
    event = Event(Name=name, Location=location, Description=description, Date=date, people_id=person_id)
    session.add(event)
    session.commit()


def show_events():
    events = session.query(Event).all()
    for e in events:
        print(e)


def add_gift(name, price, link):
    gift = Gift(Name=name, Price=price, Link=link)
    session.add(gift)
    session.commit()


def show_gifts():
    gifts = session.query(Gift).all()
    for gift in gifts:
        print(gift)


def main():
    Base.metadata.create_all(engine)
    main_menu()



if __name__ == "__main__":
    main()
