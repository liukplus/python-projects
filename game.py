import random
from player import Randomplayer,Computerplayer
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('|'+'|'.join(row)+'|')
    @staticmethod
    def print_board_nums():
        nums_board = [[str(i) for i in range(j*3+1,(j+1)*3+1)] for j in  range(3)]
        for row in nums_board:
            print('|'+'|'.join(row)+'|')
    
    def available_moves(self):
        return [i for i,spot in enumerate(self.board) if spot==' ']
    def empty_square(self):
        return ' ' in self.board
    def num_empty_square(self):
        return len(self.available_moves())
    def make_move(self,letter,square):
        if ' '== self.board[square]:
            self.board[square]=letter
            if self.winner(letter,square):
                self.current_winner=letter
            return True
        return False
    def winner(self,letter,square):
        row_ind = square//3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        col_ind = square%3
        col = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in col]):
            return True
        if square%2==0:
            diagnol1 = [self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in diagnol1]):
                return True
            diagnol2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diagnol2]):
                return True
        return False
def play(game,o_player,x_player,print_game=True):
    if print_game:
        game.print_board_nums()
    letter = 'o'
    while game.empty_square():
        if letter=='o':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(letter,square):
            if print_game:
                print(letter+f'makes a move to square{square}')
                game.print_board()
                print('')
            if game.current_winner:
                if print_game:
                    print("You win!Congratulations!!!"if letter == 'o' else "Computer wins!")
                return letter
            if letter=='o':
                letter = 'x'
            else:
                letter = 'o'
    if print_game:
        print('It\'s a tie')
if __name__=='__main__':
   x_player = Randomplayer('x')
   o_player = Computerplayer('o')
   t = TicTacToe()
   play(t,o_player,x_player,print_game=True) 
