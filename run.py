# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

SIZE = 6
NUMSHIPS = 4




class GridBuilder:
    """
    Build the game grid
    """
    def __init__(self, my_name, color, SIZE, NUMSHIPS):
        self.name = my_name
        self.color = color
        self.grid = SIZE    
        self.numships = NUMSHIPS    
        self.battleBoard = [['0' for x in range(SIZE)] for y in range(SIZE)]
        

    def printGrid(self):
        """ Build and print the computer and player grids"""
        print(f'{self.name} grid')
        for row in self.battleBoard:
            print("".join(row))
        print('\n')


def RunGame():
    print('Welcome to Battleship! Destroy the Enemy fleet!')
    print('Empty sea is 0, ship loc is S, hit is *, miss is X' )
    playerBoard = GridBuilder('player', 'Blue', SIZE, NUMSHIPS)
    computerBoard = GridBuilder('Computer', 'Green', SIZE, NUMSHIPS)
    GridBuilder.printGrid(playerBoard)
    GridBuilder.printGrid(computerBoard)

RunGame()
