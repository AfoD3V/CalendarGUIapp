class ListingStrategy:
    def __init__(self):
        self.events = []

    def register_event(self, event: tuple):
        self.events.append(event)

    def print_event(self, strategy: str):

        if strategy == "standard":
            prepared_event_list = _standard_format_strategy(self.events)
            for event in prepared_event_list:
                print(event)
        elif strategy == "icalendar":
            prepared_event_list = _icalendar_format_srategy(self.events)
            for event in prepared_event_list:
                print(event)


def _standard_format_strategy(registered_event_list: list) -> list:
    str_list = []
    for i in range(len(registered_event_list)):
        str_list.append(
            f"Title: {registered_event_list[i][0]}\nDate: {registered_event_list[i][1]}, {registered_event_list[i][2]}")
    return str_list


def _icalendar_format_srategy(registered_event_list: list) -> list:
    str_list = ['''
BEGIN:VCALENDAR
VERSION:2.0
BEGIN:VTIMEZONE
TZID:Europe/Warsaw
X-LIC-LOCATION:Europe/Warsaw
END:VTIMEZONE
    '''.rstrip()]

    for i in range(len(registered_event_list)):
        middle_part = f'''
BEGIN:VEVENT
DTSTART:{registered_event_list[i][1]}
DTEND:{registered_event_list[i][2]}
SUMMARY:{registered_event_list[i][0]}
END:VEVENT
        '''.strip()
        str_list.append(middle_part)

    str_list.append("END:VCALENDAR\n")

    return str_list
