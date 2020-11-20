from Controller.People_controller import add_people_from_file, show_people
from . import main_menu as m


def person_meny():
    print("Person meny".center(50, "-"), "\n")
    print("1. Lägg till personer från fil")
    print("2. Visa personer")
    print("3. Sök person")
    print("0. Huvudmeny \n")

    while True:
        val = input("Make yo choice: ")
        if val == "1":
            add_people_from_file()
        elif val == "2":
            people = show_people()
            for person in people:
                print(person)
        elif val == "3":
            pass
        elif val == "0":
            m.main_menu()
            break
        else:
            print("Trillade du på fingrarna eller!?!")
