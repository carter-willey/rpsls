from lizard import Lizard
from paper import Paper
from rock import Rock
from scissors import Scissors
from spock import Spock

class Player:
    def __init__(self):
        self.rock = Rock()
        self.scissors = Scissors()
        self.paper = Paper()
        self.lizard = Lizard()
        self.spock = Spock()

        self.name = ""
        self.chosen_gesture = ''
        self.score = 0
        self.gestures_list = [self.rock, self.paper, self.scissors, self.lizard, self.spock]
        self.gesture = None

    def choose_gesture(self):
        print("Override this method")
