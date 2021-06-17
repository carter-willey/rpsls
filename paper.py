from gesture import Gesture
class Paper(Gesture):
    def __init__(self):
        super().__init__()
        self.name = "paper"
        self.beats = ["rock", "Spock"]
        self.gets_beat_by = ["scissors", "lizard"]