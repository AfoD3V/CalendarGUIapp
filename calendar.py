class ListingStrategy:
    def __init__(self):
        self.title = []
        self.date = []
        self.time = []

    def get_data(self, title, date, time):
        self.title.append(title)
        self.date.append(date)
        self.time.append(time)

    def list_calendar(self):
        for i in range(len(self.title)):
            print(f"Title: {self.title[i]}\nDate: {self.date[i]}, {self.time[i]}")
