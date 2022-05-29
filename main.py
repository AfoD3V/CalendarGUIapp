from menu import Menu, MenuCommand, ExitCommand
from calendar import ListingStrategy

calendar = ListingStrategy()


class NewEvent(MenuCommand):
    def execute(self):
        title = input("Title: ")
        date = input("Date (DD.MM.YYYY): ")
        time = input("Time (HH:MM): ")

        calendar.get_data(title, date, time)

    def description(self):
        return "New event"


class ListCalendar(MenuCommand):
    def execute(self):
        calendar.list_calendar()

    def description(self):
        return "List calendar"


class Export(MenuCommand):
    def execute(self):
        pass

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
