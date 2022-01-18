# name: rockPaperScissors.py
# desc: code for a rock-paper-scissors game
# author: Mafaz Abrar Jan Chowdhury
# date: 12-JAN-2022

# the player class represents each player
class Player:

    # the init function takes in an int and a Hand object
    def __init__(self, number):
        # the "number" of the player i.e. which number the player is
        self.number = number
        self.hand = None
        self.victory = 0

    def pick_hand(self):
    
        while 1 == 1:
            print("Pick your hand: ")
            print("1. Rock")
            print("2. Paper")
            print("3. Scissors")
            
            print(f"Player {self.number}'s selection: ")

            self.selection = input()

            if self.selection == "1" or self.selection == "2" or self.selection == "3":
                self.selection = int(self.selection)
                break
            else:
                print("Please pick a number: 1, 2 or 3!")
            
# the Hand object is used to represent each of the Hands
# i.e. Rock, Paper and Scissors
class Hand:
    # the init function takes in 2 Hand objects
    # and sets them to be the "beaten_by" attribute
    def __init__(self, name):
        self.name = name

    def set_beats(self, beats):
        self.beats = beats

    # this function takes in a Hand object
    # and then checks it against itself to see
    # if it loses, then return True
    # else return False
    def check_victory(self, other_hand):
        if (other_hand.name == self.beats.name):
            return True
        else:
            return False

# the Game class manages the whole game
class Game:

    def __init__(self):
        # create the hands
        self.rock = Hand("rock") 
        self.paper = Hand("paper")   
        self.scissors = Hand("scissors")

        # set up the triangle
        self.rock.set_beats(self.scissors)
        self.scissors.set_beats(self.paper)
        self.paper.set_beats(self.rock)

        self.number_of_players = 0
        self.players = []

    # use a (non-standard) switch statement to
    # pick a hand 
    def hand_selection(self, number):
        switcher = {
            1: self.rock,
            2: self.paper,
            3: self.scissors
        }
        return switcher.get(number)

    # set up the game by adding players
    def setup_game(self):
        # set up the players
        print("Welcome to Rock Paper Scissors, Free For All!")
        
        while True:

            print("How many players are playing today?")
            self.number_of_players = input()

            if (self.number_of_players.isdigit()):
                self.number_of_players = int(self.number_of_players)
                break
            else:
                print("You have to pick a positive whole number!")
        
        for player_number in range(self.number_of_players):
            self.players.append(Player(player_number + 1))

    # begin the game by picking hands
    def begin_game(self):
        # to insert varibales into strings
        # add an f (for format string)
        print(f"Nice! So we have {self.number_of_players} players!")
        print("Let's begin!")
        
        # pick a hand for each player
        for player_number in range(self.number_of_players):
            current_player = self.players[player_number]
            current_player.pick_hand()
            current_player.hand = self.hand_selection(current_player.selection)

            # debug
            # print(f"[Debug] Current player hand: {current_player.hand.name}")
            # print(f"[Debug] Current player hand beats: {current_player.hand.beats.name}")
    
    # resolve the game by checking hands
    # and declaring a winner
    def resolve_game(self):
        for first_player in self.players:
            for second_player in self.players:

                # don't compare with self
                if (first_player == second_player):
                    # continue to the next iteration
                    # don't BREAK out of the loop
                    continue
                
                # get the hands
                first_hand = first_player.hand
                second_hand = second_player.hand

                # debug
                # print(f"[Debug] First Player: {first_player.number}")
                # print(f"[Debug] First Player's hand: {first_hand.name}")
                # print(f"[Debug] Second Player: {second_player.number}")
                # print(f"[Debug] Second Player's hand: {second_hand.name}")

                # check victory
                if (first_hand.check_victory(second_hand)):
                    first_player.victory += 1
                else:
                    first_player.victory -= 1

                # debug 
                # print(f"[Debug] First Player Victory status: {str(first_player.victory)}")
                # print(f"[Debug] Second Player Victory status: {str(second_player.victory)}")
               
        # set the default output    
        resolve_string = "No one wins!"

        # create variables to keep track of victory
        max_score = 0
        victor = None

        # cycle through players, find highest score
        for player in self.players:
            if (player.victory == max_score):
                victor = None
            if (player.victory >  max_score):
                max_score = player.victory
                victor = player

        # if victor exists, print victor name
        if (victor != None):
            resolve_string = f"Player {victor.number} wins!"
        
        # print output
        print(resolve_string)
            
def main():
    game = Game()
    game.setup_game()
    game.begin_game()
    game.resolve_game()
main()