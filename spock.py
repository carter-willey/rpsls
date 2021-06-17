from gesture import Gesture
class Spock(Gesture):
    def __init__(self):
        super().__init__()
        self.name = "Spock"
        self.beats = ["scissors", "rock"]
        self.gets_beat_by = ["lizard", "paper"]