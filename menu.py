class Menu:
    def __init__(self):
        self._commands = []     # lista komend
        self._should_run = True     # czy ma działać

    def run(self):
        while self._should_run:
            print(" Menu\n======")

            for i, cmd in enumerate(self._commands):
                print("{}. {}".format(i, cmd.description()))

            wybor = int(input("Wybor: "))
            if wybor < 0 or wybor >= len(self._commands):
                print("Nieznana opcja")
            else:
                self._commands[wybor].execute()

    def stop(self):
        self._should_run = False

    def register(self, command):
        self._commands.append(command)


class MenuCommand:

    def execute(self):
        raise NotImplementedError("you should implement this method in subclass")

    def description(self):
        raise NotImplementedError("you should implement this method in subclass")


class ExitCommand(MenuCommand):
    def __init__(self, menu):
        self._menu = menu

    def execute(self):
        self._menu.stop()

    def description(self):
        return "Exit"
