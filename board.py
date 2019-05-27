from copy import deepcopy
from os import system
from random import randint, seed

MAX_ROW = 4
MAX_COL = 4
SHUFFLE = 1000

"""
                     [[1, 2, 3, 4],
                      [5, 6, 7, 8],
                      [9, 10, 11, 12],
                      [13, 14, 15, "○"]]


                     [["1", "2", "3", "4"],
                     ["5", "6", "7", "8"],
                     ["9", "10", "11", "12"],
                     ["13", "14", "15", ""]]
"""
class Board:
    """ Model of the board"""
    def __init__(self):
        # The board
        self.goal = [[" 1", " 2", " 3", " 4"],
                     [" 5", " 6", " 7", " 8"],
                     [" 9", "10", "11", "12"],
                     ["13", "14", "15", " ▫"]]

        self.board = deepcopy(self.goal)
        self.empty_loc = [MAX_ROW - 1, MAX_COL - 1]
        self.legal_moves = {0: self.move_up, 1: self.move_down, 2: self.move_left, 3: self.move_right}

    def __repr__(self):
        # Represent the board
        for x in range(MAX_ROW):
            for y in range(MAX_COL):
                print(self.board[x][y], end=" ")
            print()

        return ""

    def movements(self, board, empty_loc, x, y):
        #Check if move is legal (if its corner you cant move further etc.)
        if empty_loc[0] + x < 0 or empty_loc[0] + x > 3 or empty_loc[1] + y < 0 or empty_loc[1] + y > 3:
            return board, empty_loc

        #Swapping empty space 0 refers to the rows, 1 refers to the columns
        board[empty_loc[0]][empty_loc[1]], board[empty_loc[0] + x][empty_loc[1] + y] \
        = board[empty_loc[0] + x][empty_loc[1] + y], board[empty_loc[0]][empty_loc[1]]

        #Updating position of the empty space
        empty_loc[0] += x
        empty_loc[1] += y

        return board, empty_loc


    def move_up(self, board, empty_loc):
        return self.movements(board, empty_loc, -1, 0)

    def move_down(self, board, empty_loc):
        return self.movements(board, empty_loc, 1, 0)

    def move_left(self, board, empty_loc):
        return self.movements(board, empty_loc, 0, -1)

    def move_right(self, board, empty_loc):
        return self.movements(board, empty_loc, 0, 1)

    def screen_refresh(self):
        system('cls')
        print('''
            This is 15 game puzzle
            If you want to end the game press Esc
            ''')
        print(self)
        #Cheking if game is over
        if self.board == self.goal:
            print("\nGame over.\nYou won!")
            return False

        return True

    #Randomize the board using legal moves (so its solvable)
    def randomize(self):
        seed()
        for i in range(SHUFFLE):
            move = randint(0, 3)
            self.legal_moves[move](self.board, self.empty_loc)

        # Move the empty space to the lower right corner (Optionally. It's only for aesthetic purposes)
        for i in range(MAX_ROW):
            self.legal_moves[1](self.board, self.empty_loc)

        for i in range(MAX_COL):
            self.legal_moves[3](self.board, self.empty_loc)

    def solve(self):
        self.board = deepcopy(self.goal)