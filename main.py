from menu import Menu, MenuCommand, ExitCommand
from calendar import ListingStrategy
import re
import datetime

calendar = ListingStrategy()


class NewEvent(MenuCommand):
    def execute(self):
        status = False
        while not status:
            # Checking for title if correct
            title = input("Title: ")
            title_check = re.findall("[a-zA-Z0-9-,. ]", title)
            if len(title) != len(title_check):
                print("\nInvalid input\n")
                return
            # checking for date if format and real date is valid
            date = input("Date (DD.MM.YYYY): ")
            date_check = re.findall("[0-9.]", date)
            if len(date) != 10:
                print("\nInvalid input\n")
                return
            elif len(date) != len(date_check):
                print("\nInvalid input\n")
                return
            try:
                day, month, year = date.split('.')
                datetime.datetime(int(year), int(month), int(day))
            except ValueError:
                print("\nInvalid input\n")
                return
            # Checking time for correct format and correct time
            time = input("Time (HH:MM): ")
            time_check = re.findall("[0-9:]", time)
            if len(time) != 5:
                print("\nInvalid input\n")
                return
            elif len(time) != len(time_check):
                print("\nInvalid input\n")
                return
            try:
                hour, minute = time.split(':')
                datetime.time(int(hour), int(minute))
            except ValueError:
                print("\nInvalid input\n")
                return
            status = True

        new_event = (title, date, time)
        calendar.register_event(new_event)

    def description(self):
        return "New event"


class ListCalendar(MenuCommand):
    def execute(self):
        calendar.print_event("standard")

    def description(self):
        return "List calendar"


class Export(MenuCommand):
    def execute(self):
        calendar.print_event("icalendar")

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
