from player import Player
class Human(Player):
    def __init__(self):
        super().__init__()
        self.value = "human"

    def display_gestures(self):
        i = 1
        print(f"{self.name}: Which gesture would you like to choose?")
        for gesture in self.gestures_list:
            print(f"{i}. {gesture}")
            i += 1
        self.choose_gesture()

    def choose_gesture(self):
        response = input(f"{self.name}, please enter a number for the corresponding gesture you would like: ")
        while response != "1" and response != "2" and response != "3" and response != "4" and response != "5":
            response = input(f"{self.name}, please enter a number for the corresponding gesture you would like: ")
        response = int(response)
        self.chosen_gesture = self.gestures_list[response - 1]

    def get_name(self, number):
        self.name = input(f"What is your name Player {number}?: ")