class ListingStrategy:
    def __init__(self):
        self.title = []
        self.date = []
        self.time = []

    ### dodaj funkcje glowna wybierajaca strategie
    def list_calendar(self, title, date, time):
        self.title.append(title)
        self.date.append(date)
        self.time.append(time)

    ### zamien na strategie
    def standar_format(self):
        for i in range(len(self.title)):
            print(f"Title: {self.title[i]}")
            print(f"Date: {self.date[i]}, {self.time[i]}")

    ### zamien na strategie
    def icalendar_format(self):
        print("BEGIN:VCALENDAR")
        print("VERSION:2.0")
        print("BEGIN:VTIMEZONE")
        print("TZID:Europe/Warsaw")
        print("X-LIC-LOCATION:Europe/Warsaw")
        print("END:VTIMEZONE")

        for i in range(len(self.title)):
            print("BEGIN:VEVENT")
            print(f"DTSTART:{self.date[i]}")
            print(f"DTEND:{self.date[i]}")
            print(f"SUMMARY:{self.title[i]}")
            print("END:VEVENT")
        print("END:VCALENDAR")
