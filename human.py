from player import Player
class Human(Player):
    def __init__(self):
        super().__init__()

    def display_gestures(self):
        i = 1
        print(f"{self.name}: Which gesture would you like to choose?")
        for gesture in self.gestures_list:
            print(f"{i}. {gesture}")
            i += 1
        self.choose_gesture()

    def choose_gesture(self):
        response = int(input(f"{self.name}, please enter a number for the corresponding gesture you would like: "))
        self.chosen_gesture = self.gestures_list[response - 1]
        print(self.gestures_list[response - 1])
    def set_gesture_class(self):

        pass
    def get_name(self, number):
        self.name = input(f"What is your name Player {number}?: ")