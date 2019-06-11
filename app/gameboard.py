"""
Ship
Player
Board
"""

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
        
        grid = []
        for row_index in range(self.height):
            new_row = []
            for col_index in range(self.width):
                new_row.append(BLANK)
            grid.append(new_row)
        self.grid = grid
        self.ship_index = grid[ship_col][ship_row]
        return self.grid


    def user_input():
        coordinates = input("Enter coordinates: ")
        c_col = coordinates[0]
        c_row = coordinates[1]
        user_index = grid[c_col][c_row]
        if user_index = ship_index:
            print("You won.")
        else:
            user_index = MISS
        if c_col == self.ship_col and c_row == self.ship_row:
            index_
        else:
            pass
        
        
    


if __name__ == '__main__':
    g = GameBoard()
    print(g)
    for row in g.board():
        print(row)