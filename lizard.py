from gesture import Gesture
class Lizard(Gesture):
    def __init__(self):
        super().__init__()
        self.name = "lizard"
        self.beats = ["Spock", "paper"]
        self.gets_beat_by = ["rock", "scissors"]
    def __str__(self):
        return "Lizard"