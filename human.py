from player import Player
class Human(Player):
    def __init__(self):
        super().__init__()
        self.get_name()

    def display_gestures(self):
        i = 1
        print(f"{self.name}: Which gesture would you like to choose?")
        for gesture in self.gestures:
            print(f"{i}. {gesture}")
            i += 1
        self.choose_gesture()

    def choose_gesture(self):
        self.chosen_gesture = int(input("Please enter a number for the corresponding gesture you would like: "))

    def get_name(self):
        self.name = str(input("What is your name?: "))