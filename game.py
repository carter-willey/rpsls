from human import Human
from ai import AI

class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = None
        self.player_one.display_gestures()

    def display_welcome(self):
        print("Hello and welcome to Rock, Paper, Scissors, Lizard, Spock!")

    def run_game(self):
        # Intro
        #Display welcome
        #Instructions
        #Pick game mode - single player or multiplayer

        #Game Rounds
        #Player one chooses gesture
        #player two chooses gesture
        #determine winner of round, give winner score
        #loop to continue gameplay until best of three


        #End Game
        #display winner of game
        pass

    def check_gestures(self):
        #logic of what beats what
        pass
    def choose_game_mode(self):
        #get input
        #if single
        pass