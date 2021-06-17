from human import Human
from ai import AI
import time


class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = None
        self.run_game()
        self.game_state = None

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
        print(self.game_state)
        while self.game_state == True:
            #Game Rounds
            #Player one and two choose gesture
            self.player_one.display_gestures()
            if self.player_two.value == "human":
                self.player_two.display_gestures()
            else:
                self.player_two.choose_gesture()

            #determine winner of round, give winner score
            self.check_gestures()

            #loop to continue gameplay until best of three

        print("Would you like to play again?")
        play_again = input("Enter '1' for yes or '2' for no: ")
        while play_again != "1" and play_again != "2":
            print("Please enter either '1' or '2'")
            play_again = input("Enter '1' for yes or '2' for no: ")

        if play_again == "1":
            self.run_game()
        else:
            print("Thank you for playing! Goodbye!")



    def check_gestures(self):
        if self.player_one.chosen_gesture.name == self.player_two.chosen_gesture.name:
            print(f"Both players picked {self.player_one.chosen_gesture}. This round is a draw")
        elif (self.player_one.chosen_gesture.name == self.player_two.chosen_gesture.gets_beat_by[0]) or (self.player_one.chosen_gesture.name == self.player_two.chosen_gesture.gets_beat_by[1]):
            self.player_one.score += 1
            print(f"{self.player_one.name} won the round! {self.player_one.name} chose {self.player_one.chosen_gesture}, which beats {self.player_two.name}'s {self.player_two.chosen_gesture}!")
            if self.player_one.score == 2:
                print(f"{self.player_one.name} Wins! with a score of {self.player_one.score} to {self.player_two.score}")
                self.game_state = False
            else:
                print(f"With that win, {self.player_one.name} now has {self.player_one.score} point(s)!")
        elif (self.player_one.chosen_gesture.name == self.player_two.chosen_gesture.beats[0]) or (self.player_one.chosen_gesture.name == self.player_two.chosen_gesture.beats[1]):
            print(f"{self.player_two.name} won the round! {self.player_two.name} chose {self.player_two.chosen_gesture}, which beats {self.player_one.name}'s {self.player_one.chosen_gesture}!")
            self.player_two.score += 1
            if self.player_two.score == 2:
                print(f"{self.player_two.name} Wins! with a score of {self.player_two.score} to {self.player_one.score}")
                self.game_state = False
            else:
                print(f"With that win, {self.player_two.name} now has {self.player_two.score} point(s)!")
    def choose_game_mode(self):
        print("What game mode would you like to play?")
        game_mode = input("Please enter '1' for Single player or '2' for Two player: ")
        while game_mode != "1" and game_mode != "2":
            print("Please enter either '1' or '2'")
            game_mode = input("Please enter '1' for Single player or '2' for Two player: ")
        self.game_state = True

        if game_mode == "1":
            self.player_one.get_name("One")
            self.player_two = AI()
        else:
            self.player_one.get_name("One")
            self.player_two = Human()
            self.player_two.get_name("Two")
