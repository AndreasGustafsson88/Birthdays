from UI.event_meny import event_meny
from UI.person_meny import person_meny
from UI.present_meny import present_meny


def main_menu():
    print("Välkommen till din lokala kalender!".center(70, "-"), "\n")
    print("1. Personer")
    print("2. Presenter")
    print("3. Händelser")
    print("0. Get me outta here \n")

    while True:
        val = input("Make yo choice: ")
        if val == "1":
            person_meny()
        elif val == "2":
            present_meny()
        elif val == "3":
            event_meny()
        elif val == "0":
            break
        else:
            print("Är det svårt att välja mellan siffrorna 1-4?")




