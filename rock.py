from gesture import Gesture
class Rock(Gesture):
    def __init__(self):
        super().__init__()
        self.name = "rock"
        self.beats = ["scissors", "lizard"]
        self.gets_beat_by = ["paper", "Spock"]

    def __str__(self):
        return "Rock"