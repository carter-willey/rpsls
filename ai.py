from player import Player
import random

class AI(Player):
    def __init__(self):
        super().__init__()

    def choose_gesture(self):
        random_index = random.randint(0,4)
        self.chosen_gesture = self.gestures[random_index]
        print(self.chosen_gesture)
