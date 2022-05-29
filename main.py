# wzorzec polecenie
# kazdy wpis w menu jest osobnym obiektem
#
# 1. tekst programisty
# 2. tekst ....
# 3. ....
#
# Wybor: 1
#
# 1. tekst programisty
# 2. tekst ....
# 3. exit
#
# Wybor: 3

from menu import Menu, MenuCommand, ExitCommand


class NewEvent(MenuCommand):
    def execute(self):
        pass

    def description(self):
        return "New event"


def main():
    menu = Menu()

    menu.register(NewEvent())
    menu.register(ExitCommand(menu))

    menu.run()


if __name__ == "__main__":
    main()
