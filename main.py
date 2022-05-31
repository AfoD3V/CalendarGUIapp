from menu import Menu, MenuCommand, ExitCommand
from calendar import ListingStrategy

calendar = ListingStrategy()


class RegisteredEvents:
    def __init__(self):
        self.events = []

    def create_event(self, title, date, time):
        


class NewEvent(MenuCommand):
    def execute(self):
        title = input("Title: ")
        date = input("Date (DD.MM.YYYY): ")
        time = input("Time (HH:MM): ")

        calendar.list_calendar(title, date, time)

    def description(self):
        return "New event"


class ListCalendar(MenuCommand):
    def execute(self):
        calendar.standar_format()

    def description(self):
        return "List calendar"

#dodaj weryfikacje danych

class Export(MenuCommand):
    def execute(self):
        calendar.icalendar_format()

    def description(self):
        return "Export calendar to iCalendar"


def main():
    menu = Menu()

    menu.register(NewEvent())
    menu.register(ListCalendar())
    menu.register(Export())
    menu.register(ExitCommand(menu))

    menu.run()


if __name__ == "__main__":
    main()
