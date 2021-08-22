import math
import random
class Player:
    def __init__(self,letter):
        self.letter = letter
    def get_move(self,game):
        pass

class Randomplayer(Player):
    def __init__(self,letter):
        super().__init__(letter)
    def get_move(self,game):
        square = random.choice(game.available_moves())
        return square

class Computerplayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        valid_square = False
        square = input(f"It's your turn ({self.letter}). Input move (1-9):")
        while not valid_square:
                val = int(square) - 1
                try:
                    if val not in game.available_moves():
                        raise ValueError
                    valid_square = True
                except ValueError:
                    square = input("Invalid number! Enter again:")
        return val
