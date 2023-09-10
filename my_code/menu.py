class Menu:
    """A class used for representing menu object"""

    def __init__(self):
        self._commands = []
        self._should_run = True

    def run(self):
        """Running menu method"""
        while self._should_run:
            print("====== Menu ======")

            for i, cmd in enumerate(self._commands, 1):
                print("{}. {}".format(i, cmd.description()))

            pick_option = int(input("\nSelect option [1-4]: "))
            if pick_option <= 0 or pick_option > len(self._commands):
                print("\nWrong option!\n")
            else:
                self._commands[pick_option - 1].execute()

    def stop(self):
        """Simple aborting menu method"""
        self._should_run = False

    def register(self, command):
        """Method for registering new object"""
        self._commands.append(command)


class MenuCommand:
    """Class representing in menu command"""

    def execute(self):  # Inside block code is going to be executed on "push"
        raise NotImplementedError("You should implement this method in subclass")

    def description(self):  # Description of button which you can see in 'live' menu
        raise NotImplementedError("You should implement this method in subclass")


# Menu button - aborting menu running
class ExitCommand(MenuCommand):
    """Exit - menu command"""

    def __init__(self, menu):
        self._menu = menu

    def execute(self):
        self._menu.stop()

    def description(self):
        return "Exit"
