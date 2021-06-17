from gesture import Gesture
class Scissors(Gesture):
    def __init__(self):
        super().__init__()
        self.name = "scissors"
        self.beats = ["paper", "lizard"]
        self.gets_beat_by = ["rock", "Spock"]