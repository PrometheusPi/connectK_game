"""
This game is inspired by a job interview test reported by Johannes Pausch.

You have a (infinitly - here finite) horizontal field and try to connect k points.
Each player takes turns to add their stones. In contrast to classical connect-4, stones are added beneeth existing stones and push up the stones of the collumn.
"""

import os
import time

#print('Coding Ninjas!\n'*5)

#time.sleep(5)

#os.system('clear')

class Board:
    """
    class that holds the board status
    """
    win_length = 4

    def __init__(self, N_colums, N_rows=20):
        self.N_colums = N_colums
        self.N_rows = N_rows

        self.board = []
        for i in range(self.N_rows):
            self.board.append([0] * self.N_colums)
        self.state = "ungoing"



    def move_up(self, player, column):
        if self.board[-1][column] != 0:
            print("to many pieces in column", column, "the game ends in a draw")
            self.state = "draw"
        else:
            for i in range(self.N_rows -2, -1, -1):
                #print(self.board[i+1][column], self.board[i][column])
                self.board[i+1][column] = self.board[i][column]

            #print(self.board)
            self.board[0][column] = player
            #print(self.board)
    #def test(self):
    #    for i in range(self.N_rows):


    def determine_win(self):
        if self.state != "ungoing":
            return None

        # check columns:
        for i in range(self.N_rows):
            test_stack = []
            for j in range(self.N_colums):
                test_stack.append( self.board[i][j] )
                if len(test_stack) >= self.win_length:
                    if test_stack[-self.win_length:] == [1] * self.win_length:
                        print("found win 1 - columns")
                        if self.state == "ungoing":
                            self.state = 1
                        elif self.state == 2:
                            self.state = "Draw"
                    elif test_stack[-self.win_length:] == [2] * self.win_length:
                        print("found win 2 - columns")
                        if self.state == "ungoing":
                            self.state = 2
                        elif self.state == 1:
                            self.state = "Draw"
            #print(test_stack)

        #print("#####")
        # check rows:
        for i in range(self.N_colums):
            test_stack = []
            for j in range(self.N_rows):
                test_stack.append( self.board[j][i] )
                if len(test_stack) >= self.win_length:
                    if test_stack[-self.win_length:] == [1] * self.win_length:
                        print("found win 1 - rows")
                        if self.state == "ungoing":
                            self.state = 1
                        elif self.state == 2:
                            self.state = "Draw"
                    elif test_stack[-self.win_length:] == [2] * self.win_length:
                        print("found win 2 - rows")
                        if self.state == "ungoing":
                            self.state = 2
                        elif self.state == 1:
                            self.state = "Draw"
            #print(test_stack)



    def place(self, player, column):
        if not player in [1, 2]:
            raise Exception('player must be 1 or 2')

        if column < 0 or column > self.N_colums:
            raise Exception('column must be between 0 and', self.N_colums - 1)

        self.move_up(player, column)

        self.determine_win()

        if self.state in [1, 2]:
            print("Player {} has won!!!".format(result))
        elif self.state == "Draw":
            print("No one won - it's a draw!!!")





import sys

def clean_screen():
    """
    clean terminal screen
    """
    sys.stdout.write("\33[H\33[2J") #"\33" is the ESC character
    sys.stdout.flush()

if __name__ == "__main__":

    if False:

        for step in range(100):
            for i in range(5):
                print("\n")
            print("x"*step)
            print("\n")
            for i in range(5):
                print("\n")
            time.sleep(0.2)
            clean_screen()
