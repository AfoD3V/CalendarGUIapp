class Menu:
    def __init__(self):
        self._commands = []
        self._should_run = True

    def run(self):
        """Function for running menu"""
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
        """Aborting menu"""
        self._should_run = False

    def register(self, command):
        """Function for registering menu command"""
        self._commands.append(command)


class MenuCommand:
    """Class which is creating menu button, not implementing both of methods will result in rising error"""
    def execute(self):  # Inside block code is going to be executed on "push"
        raise NotImplementedError("You should implement this method in subclass")

    def description(self):  # Description of button which you can see in 'live' menu
        raise NotImplementedError("You should implement this method in subclass")


# Menu button - aborting menu running
class ExitCommand(MenuCommand):
    def __init__(self, menu):
        self._menu = menu

    def execute(self):
        self._menu.stop()

    def description(self):
        return "Exit"
