from player import Player
class Human(Player):
    def __init__(self):
        super().__init__()

    def display_gestures(self):
        i = 1
        print(f"{self.name}: Which gesture would you like to choose?")
        for gesture in self.gestures:
            print(f"{i}. {gesture}")
            i += 1
        self.choose_gesture()

    def choose_gesture(self):
        response = int(input("Please enter a number for the corresponding gesture you would like: "))
        self.chosen_gesture = self.gestures[response - 1]
    def get_name(self, number):
        self.name = str(input(f"What is your name Player {number}?: "))