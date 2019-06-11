"""
Ship
Player
Board
"""
import sys
import os

BLANK = ' '
SHIP  = 'S'
MISS  = 'M'
HIT   = 'X'


class GameBoard:

    def __init__(self, width=5, height=5):
        self.width = width
        self.height = height
        self.ship_row = 1
        self.ship_col = 1
        
        self.grid = []

        for row_index in range(self.height):
            new_row = []
            for col_index in range(self.width):
                new_row.append(BLANK)
            self.grid.append(new_row)
        #self.grid = grid
        self.ship_index = self.grid[self.ship_col][self.ship_row]
        

    def user_input(self):
        print(self.ship_index)
        while True:
            for row in self.grid:
                print(row)
            coordinates = input("Enter coordinates: ")
            c_col = int(coordinates[0]) - 1
            c_row = int(coordinates[1]) - 1

            print(c_col, c_row)
            if c_col == self.ship_col and c_row == self.ship_row:
                print("You won.")
                self.grid[self.ship_row][self.ship_col]="X"
                for row in self.grid:
                    print(row)
                sys.exit()
            else:
                self.grid[c_col][c_row]="M"
                os.system('clear')


                
            
    


if __name__ == '__main__':
    g = GameBoard()
    g.user_input()
    