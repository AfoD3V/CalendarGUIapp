class ListingStrategy:
    def __init__(self):
        self.events = []

    def register_event(self, event: tuple):
        """Function for registering new event on the list"""
        self.events.append(event)

    def print_event(self, strategy: str):
        """General function for printing registered event in a format defined by strategy"""
        if strategy == "standard":
            prepared_event_list = _standard_format_strategy(self.events)
            for event in prepared_event_list:
                print(event)
        elif strategy == "icalendar":
            prepared_event_list = _icalendar_format_srategy(self.events)
            for event in prepared_event_list:
                print(event)


def _standard_format_strategy(registered_event_list: list) -> list:
    """Function for inside use, preparing data for standard format"""
    str_list = []
    for i in range(len(registered_event_list)):
        str_list.append(
            f"Title: {registered_event_list[i][0]}\nDate: {registered_event_list[i][1]}, {registered_event_list[i][2]}")
    return str_list


assert _standard_format_strategy([]) == []
assert _standard_format_strategy([('sample_title', '12.12.2020', '12:45')]) == (["Title: sample_title\n"
                                                                                 "Date: 12.12.2020, 12:45"])


def _icalendar_format_srategy(registered_event_list: list) -> list:
    """Function for inside use, preparing data for icalendar format"""
    # Start of string, always same for every case
    str_list = ['''
BEGIN:VCALENDAR
VERSION:2.0
BEGIN:VTIMEZONE
TZID:Europe/Warsaw
X-LIC-LOCATION:Europe/Warsaw
END:VTIMEZONE
    '''.rstrip()]

    # Loop which is iterating through registered events
    for i in range(len(registered_event_list)):
        day, month, year = registered_event_list[i][1].split('.')
        hour, minute = registered_event_list[i][2].split(':')
        middle_part = f'''
BEGIN:VEVENT
DTSTART:{year + month + day + "T" + hour + minute + "00"}
DTEND:{year + month + day + "T" + hour + minute + "00"}
SUMMARY:{registered_event_list[i][0]}
END:VEVENT
        '''.strip()
        str_list.append(middle_part)

    # Ending string, like start same for every case
    str_list.append("END:VCALENDAR\n")
    if len(str_list) <= 2:
        return []
    else:
        return str_list


def testing_function 
assert _icalendar_format_srategy([]) == []

test_list = [
    '\nBEGIN:VCALENDAR\nVERSION:2.0\nBEGIN:VTIMEZONE\nTZID:Europe/Warsaw\nX-LIC-LOCATION:Europe/Warsaw\nEND:VTIMEZONE',
    'BEGIN:VEVENT\nDTSTART:20201212T124500\nDTEND:20201212T124500\nSUMMARY:sample_title\nEND:VEVENT',
    'END:VCALENDAR\n'
]

assert _icalendar_format_srategy([('sample_title', '12.12.2020', '12:45')]) == test_list, (
    f"\nExpected: {test_list}\n     Got: {_icalendar_format_srategy([('sample_title', '12.12.2020', '12:45')])}")
