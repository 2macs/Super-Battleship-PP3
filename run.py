# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

ROWS = 10
COLS = 10


class GridBuilder:
    """
    Build the game grid
    """
    def __init__(self, my_name, color, rows, cols):
        self.name = my_name
        self.color = color
        self.rows = rows
        self.cols = cols
        print('Grid Builder class is called..')
        print(f'Name is {self.name}, color is {self.color}, rows are {self.rows}, cols are {self.cols}.')


GridBuilder('player', 'Blue', ROWS, COLS)
GridBuilder('Computer', 'Green', ROWS, COLS)