from collections import defaultdict
from Data.Models.People import People
from Data.db import *


def add_people(first_name, last_name, DOB, relation):
    user = People(
        FirstName=first_name,
        LastName=last_name,
        DOB=DOB,
        Relation=relation
    )
    session.add(user)
    session.commit()




