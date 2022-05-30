class ListingStrategy:
    def __init__(self):
        self.title = []
        self.date = []
        self.time = []
    ### dodaj funkcje glowna wybierajaca strategie
    def get_data(self, title, date, time):
        self.title.append(title)
        self.date.append(date)
        self.time.append(time)

    ### zamien na strategie
    def list_calendar(self):
        for i in range(len(self.title)):
            print(f"Title: {self.title[i]}\nDate: {self.date[i]}, {self.time[i]}")

    ### zamien na strategie
    def icalendar_export(self):
        print("""BEGIN:VCALENDAR
VERSION:2.0
BEGIN:VTIMEZONE
TZID:Europe/Warsaw
X-LIC-LOCATION:Europe/Warsaw
END:VTIMEZONE""")

        for i in range(len(self.title)):
            print(f"""BEGIN:VEVENT
DTSTART:{self.date[i]}
DTEND:{self.date[i]}
SUMMARY:{self.title[i]}
END:VEVENT""")
        print("END:VCALENDAR")
