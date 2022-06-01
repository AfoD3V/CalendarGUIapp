class ListingStrategy:
    def __init__(self):
        self.events = []

    def register_event(self, event: tuple):
        self.events.append(event)

    def print_events(self):
        pass


def standar_format_strategy():
    for i in range(len(self.title)):
        print(f"Title: {self.title[i]}")
        print(f"Date: {self.date[i]}, {self.time[i]}")


# def icalendar_format(self):
#     print("BEGIN:VCALENDAR")
#     print("VERSION:2.0")
#     print("BEGIN:VTIMEZONE")
#     print("TZID:Europe/Warsaw")
#     print("X-LIC-LOCATION:Europe/Warsaw")
#     print("END:VTIMEZONE")
#
#     for i in range(len(self.title)):
#         print("BEGIN:VEVENT")
#         print(f"DTSTART:{self.date[i]}")
#         print(f"DTEND:{self.date[i]}")
#         print(f"SUMMARY:{self.title[i]}")
#         print("END:VEVENT")
#     print("END:VCALENDAR")
