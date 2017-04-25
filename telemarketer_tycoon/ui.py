import sys
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

    def do_quit(self, args):
        """Quit the game"""
        raise GameOver