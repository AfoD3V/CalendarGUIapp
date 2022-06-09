from menu import Menu, MenuCommand, ExitCommand
from calendar import ListingStrategy
import re
import datetime
import tkinter as tk

calendar = ListingStrategy()


# To do zmodyfikowac klase wyzej moze byc niepotrzebna
# dodac komentarze
# ustawic wartosci typowania oraz return dla funkcji

class MainApplication(tk.Frame):
    """GUI class"""
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # Labels for windows description
        self.label_new_event = tk.Label(root, text="Title: ", font="none 9 bold")
        self.label_date = tk.Label(root, text="Date (DD.MM.YYYY): ", font="none 9 bold")
        self.label_time = tk.Label(root, text="Time (HH:MM): ", font="none 9 bold")
        self.label_new_event.grid(row=0, column=0)
        self.label_date.grid(row=1, column=0)
        self.label_time.grid(row=2, column=0)

        # Entry windows
        self.new_event = tk.Entry(root, width=35, borderwidth=5)
        self.date = tk.Entry(root, width=35, borderwidth=5)
        self.time = tk.Entry(root, width=35, borderwidth=5)
        self.new_event.grid(row=0, column=1)
        self.date.grid(row=1, column=1)
        self.time.grid(row=2, column=1)

        # Buttons
        self.button_new_event = tk.Button(root, text="Register event", width=15, height=1, command=self.reg)
        self.button_list_calendar = tk.Button(root, text="List of events", width=15, height=1,
                                              command=self.registered_events_list)
        self.button_export = tk.Button(root, text="Export to iCalendar", width=15, height=1, command=self.export_events)
        self.button_exit = tk.Button(root, text="Exit", width=15, height=1, command=self.close)
        self.button_new_event.grid(row=0, column=2, sticky=tk.NSEW)
        self.button_list_calendar.grid(row=0, column=3, sticky=tk.NSEW)
        self.button_export.grid(row=1, column=2, columnspan=2, sticky=tk.NSEW)
        self.button_exit.grid(row=2, column=2, columnspan=2, sticky=tk.NSEW)

        # Output window
        self.output = tk.Text(root, width=75, height=15, wrap=tk.WORD, borderwidth=5, background="white")
        self.output.grid(row=3, column=0, columnspan=4, sticky=tk.NSEW)

    @staticmethod
    def close():
        """Static method used to exit from window"""
        root.destroy()

    def reg(self):
        """Button method for register new event"""
        self.output.delete(0.0, tk.END)
        registration_status = "Success!!"

        # Tittle check
        title_for_check = self.new_event.get()
        if DataVerification.title_check(title_for_check):
            pass
        else:
            registration_status = "Invalid input"
        # Date Check
        date_for_check = self.date.get()
        if DataVerification.date_check(date_for_check):
            pass
        else:
            registration_status = "Invalid input"
        # Time check
        time_for_check = self.time.get()
        if DataVerification.time_check(time_for_check):
            pass
        else:
            registration_status = "Invalid input"

        self.output.insert(tk.END, registration_status)
        new_event = (title_for_check, date_for_check, time_for_check)
        if registration_status == "Success!!":
            calendar.register_event(new_event)  # registering event

    def registered_events_list(self):
        """Button method for output in standard format"""
        events = calendar.print_event("standard", "gui")
        self.output.delete(0.0, tk.END)
        self.output.insert(tk.END, events)

    def export_events(self):
        """Button method for output in iCalendar format"""
        events = calendar.print_event("icalendar", "gui")
        self.output.delete(0.0, tk.END)
        self.output.insert(tk.END, events.lstrip())


class NewEvent(MenuCommand):
    """[New event] - menu button"""

    def execute(self):
        # Registering new event for in console use
        title = input("Title: ")
        if DataVerification.title_check(title):
            pass
        else:
            print("\nInvalid input\n")
            return
        date = input("Date (DD.MM.YYYY): ")
        if DataVerification.date_check(date):
            pass
        else:
            print("\nInvalid input\n")
            return
        time = input("Time (HH:MM): ")
        if DataVerification.date_check(date):
            pass
        else:
            print("\nInvalid input\n")
            return

        new_event = (title, date, time)
        calendar.register_event(new_event)

    def description(self):
        return "New event"


class ListCalendar(MenuCommand):
    """[List calendar] - menu button"""

    def execute(self):
        calendar.print_event("standard")

    def description(self):
        return "List calendar"


class Export(MenuCommand):
    """[Export] - menu button"""

    def execute(self):
        calendar.print_event("icalendar")

    def description(self):
        return "Export calendar to iCalendar"


class DataVerification:
    @staticmethod
    def title_check(title: str) -> bool:
        """Verification method to check if typed title is in correct format"""
        title_check = re.findall("[a-zA-Z0-9-,. ]", title)
        if len(title) != len(title_check):
            return False
        else:
            return True

    @staticmethod
    def date_check(date: str) -> bool:
        """Verification method to check if typed date is in correct format"""
        date_check = re.findall("[0-9.]", date)
        if len(date) != 10:
            return False
        elif len(date) != len(date_check):
            return False
        try:
            day, month, year = date.split('.')
            datetime.datetime(int(year), int(month), int(day))
            return True
        except ValueError:
            return False

    @staticmethod
    def time_check(time: str) -> bool:
        """Verification method to check if typed time is in correct format"""
        time_check = re.findall("[0-9:]", time)
        if len(time) != 5:
            return False
        elif len(time) != len(time_check):
            return False
        try:
            hour, minute = time.split(':')
            datetime.time(int(hour), int(minute))
            return True
        except ValueError:
            return False


def main():
    menu = Menu()

    menu.register(NewEvent())
    menu.register(ListCalendar())
    menu.register(Export())
    menu.register(ExitCommand(menu))

    menu.run()


if __name__ == "__main__":
    print('For console mode type "con".')
    print('For GUI mode type "gui".')
    mode = input("Mode: ")
    if mode == "con":
        main()
    elif mode == "gui":
        root = tk.Tk()
        root.title("Calendar by Roman Afonin")
        root.attributes('-topmost', True)  # making window to pop on top of tabs
        root.update()
        MainApplication(root).grid()
        root.mainloop()
    else:
        print("Not valid option")
