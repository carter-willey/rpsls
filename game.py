from human import Human
from ai import AI
import time

class Game:
    def __init__(self):
        #self.player_one = Human()
        self.player_two = None
        self.run_game()

    def display_welcome(self):
        print("Hello and welcome to Rock, Paper, Scissors, Lizard, Spock!")
    def display_rules(self):
        print("The rules are similar to your standard game of rock paper scissors. However, we have two added two more options: lizard and Spock")
        time.sleep(.75)
        print("Your standard rock, paper, scissors rules apply with the following additional rules:\n"
              "Rock crushes Lizard\n"
              "Lizard poisons Spock\n"
              "Spock smashes Scissors\n"
              "Scissors decapitates Lizard\n"
              "Lizard eats Paper\n"
              "Paper disproves Spock\n"
              "Spock vaporizes Rock\n"              )



    def run_game(self):
        # Intro
        self.display_welcome()
        time.sleep(.75)
        self.display_rules()
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