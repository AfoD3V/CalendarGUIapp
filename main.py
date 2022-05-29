from menu import Menu, MenuCommand, ExitCommand


class NewEvent(MenuCommand):
    def execute(self):
        pass

    def description(self):
        return "New event"


class ListCalendar(MenuCommand):
    def execute(self):
        pass

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
