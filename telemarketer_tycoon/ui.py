from cmd import Cmd

from telemarketer_tycoon.exceptions import GameOver


class GamePrompt(Cmd):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.prompt = "> "

    def do_continue(self, args):
        """Continue to the next week"""
        return True

    def do_c(self, args):
        """Continue to the next week"""
        return self.do_continue(args)

    def emptyline(self):
        return self.do_continue(None)

    def do_hire(self, args):
        """Hire a new caller"""
        return self.game.employee_hiring()

    def do_h(self, args):
        """Hire a new caller"""
        return self.do_hire(args)

    def do_fire(self, args):
        """Fire a caller (give their name)
        
        e.g. > fire 2
        """
        if len(args) == 0:
            print("Please give the callers name")
            return False
        return self.game.fire_caller(args[0])

    def do_stats(self, args):
        """Display caller stats"""
        return self.game.print_caller_stats()

    def do_quit(self, args):
        """Quit the game"""
        raise GameOver