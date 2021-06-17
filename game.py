from human import Human
from ai import AI
import time


class Game:
    def __init__(self):
        self.player_one = Human()
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
              "Spock vaporizes Rock")


    def run_game(self):
        # Intro & Instructions
        self.display_welcome()
        time.sleep(.75)
        self.display_rules()

        #Pick game mode - single player or multiplayer
        self.choose_game_mode()

        #Game Rounds
        #Player one and two choose gesture
        player_one_pick = self.player_one.display_gestures()
        if self.player_two == Human():
            player_two_pick = self.player_two.display_gestures()
        else:
            player_two_pick = self.player_two.choose_gesture()

        #determine winner of round, give winner score

        #loop to continue gameplay until best of three


        #End Game
        #display winner of game


    def check_gestures(self):
        #logic of what beats what
        pass
    def choose_game_mode(self):
        print("What game mode would you like to play?")
        game_mode = input("Please enter '1' for Single player or '2' for Two player: ")
        if game_mode != "1" and game_mode != "2":
            while game_mode != "1" and game_mode != "2":
                print("Please enter either '1' or '2'")
                game_mode = input("Please enter '1' for Single player or '2' for Two player: ")
            game_mode = int(game_mode)
        else:
            game_mode = int(game_mode)

        if game_mode == 1:
            self.player_one.get_name("One")
            self.player_two = AI()
        else:
            self.player_one.get_name("One")
            self.player_two = Human()
            self.player_two.get_name("Two")
