from player import Player
import random

class AI(Player):
    def __init__(self):
        super().__init__()
        self.value = 'ai'
        self.name = "Mr. Robot"

    def choose_gesture(self):
        random_index = random.randint(0,4)
        self.chosen_gesture = self.gestures_list[random_index]
        print(self.chosen_gesture)
