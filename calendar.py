import unittest


class ListingStrategy:
    def __init__(self):
        self.events = []

    def register_event(self, event: tuple):
        """Function for registering new event on the list"""
        return self.events.append(event)

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


def _icalendar_format_srategy(registered_event_list: list) -> list:
    """Function for inside use, preparing data for icalendar format"""
    # Start of string, always same for every case
    str_list = [
        "\nBEGIN:VCALENDAR\n"
        "VERSION:2.0\n"
        "BEGIN:VTIMEZONE\n"
        "TZID:Europe/Warsaw\n"
        "X-LIC-LOCATION:Europe/Warsaw\n"
        "END:VTIMEZONE".rstrip()
                ]

    # Loop which is iterating through registered events
    for i in range(len(registered_event_list)):
        day, month, year = registered_event_list[i][1].split('.')
        hour, minute = registered_event_list[i][2].split(':')
        middle_part = f"BEGIN:VEVENT\n" \
                      f"DTSTART:{year + month + day + 'T' + hour + minute + '00'}\n" \
                      f"DTEND:{year + month + day + 'T' + hour + minute + '00'}\n" \
                      f"SUMMARY:{registered_event_list[i][0]}\nEND:VEVENT".strip()
        str_list.append(middle_part)

    # Ending string, like start same for every case
    str_list.append("END:VCALENDAR\n")
    if len(str_list) <= 2:
        return []
    else:
        return str_list


class TestCalendarMethods(unittest.TestCase):

    def test_standard_format(self):
        # case_1
        self.assertEqual(_standard_format_strategy([]), [], "standard_format case_1 failed")
        # case_2
        self.assertEqual(_standard_format_strategy([('sample_title', '12.12.2020', '12:45')]),
                         ["Title: sample_title\nDate: 12.12.2020, 12:45"], "standard_format case_2 failed")

    def test_icalendar_format(self):
        # case_1
        self.assertEqual(_icalendar_format_srategy([]), [], "icalendar_format case_1 failed")
        test_list = [
            '\nBEGIN:VCALENDAR\nVERSION:2.0\nBEGIN:VTIMEZONE\nTZID:Europe/Warsaw\nX-LIC-LOCATION:Europe/Warsaw\nEND:VTIMEZONE',
            'BEGIN:VEVENT\nDTSTART:20201212T124500\nDTEND:20201212T124500\nSUMMARY:sample_title\nEND:VEVENT',
            'END:VCALENDAR\n'
        ]
        # case_2
        self.assertEqual(_icalendar_format_srategy([('sample_title', '12.12.2020', '12:45')]), test_list,
                         "icalendar_format case_2 failed")
