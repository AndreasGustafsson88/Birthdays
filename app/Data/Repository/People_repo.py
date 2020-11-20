from collections import defaultdict
from Data.db import session
from Data.Models.People import People


def add_people_from_file():
    with open("/_documents/people.txt", "r") as file:
        peoples = defaultdict()
        for column in file.readlines():
            line = column.split()
            peoples["FirstName"] = line[0]
            peoples["LastName"] = line[1]
            peoples["DOB"] = line[2]
            peoples["Relation"] = line[3]
            users = People(**peoples)
            session.add(users)
    session.commit()


def show_people():
    return session.query(People).all()

