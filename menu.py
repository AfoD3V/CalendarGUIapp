class Menu:
    def __init__(self):
        self._commands = []
        self._should_run = True

    def run(self):
        while self._should_run:
            print("====== Menu ======")

            for i, cmd in enumerate(self._commands, 1):
                print("{}. {}".format(i, cmd.description()))

            wybor = int(input("\nWybor: "))
            if wybor <= 0 or wybor > len(self._commands):
                print("\nNieznana opcja!!!\n")
            else:
                self._commands[wybor - 1].execute()

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
