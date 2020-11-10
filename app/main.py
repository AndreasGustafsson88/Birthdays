from db import session, Base, engine
from models.Events import Event
from models.People import People


def add_people(first_name, last_name, DOB, relation):
    user = People(
        FirstName=first_name,
        LastName=last_name,
        DOB=DOB,
        Relation=relation
    )
    session.add(user)
    session.commit()


def show_people():
    people = session.query(People).all()
    for p in people:
        print(p)


def add_event(name, location, description, date, person_id):
    event = Event(Name=name, Location=location, Description=description, Date=date, people_id=person_id)
    session.add(event)
    session.commit()


def show_events():
    events = session.query(Event).all()
    for e in events:
        print(e)


def main():
    Base.metadata.create_all(engine)
    # add_people("Cecilia", "Melin", "1993-03-27", "kjäreste")
    # add_event("Födelsedag", "Ulricehamn", "Fyller 33 år gammel", "2021-04-01", 1)
    show_events()
    show_people()

if __name__ == "__main__":
    main()
