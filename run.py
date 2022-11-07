# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
import os

SIZE = 6
NUMSHIPS = 4
game_state_over = False 

width = os.get_terminal_size().columns


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
        self.shipPositions = []       
        

    def printGrid(self):
        """ Build and print the computer and player grids"""
        print(f'{self.name} grid')
        for row in self.battleBoard:
            print("".join(row))
        print('\n')
    
    def PositionShips(self):
        """ Randomly locate NUMSHIPS of ships on the board"""
        i = 0 
        while i < NUMSHIPS:
            random_row = random.randint(0,SIZE - 1)
            random_col = random.randint(0,SIZE - 1)
            thisLoc = [random_row,random_col]
            print(F'Rand row is {random_row}, random column is {random_col}')
            self.shipPositions.append(thisLoc)
            i += 1
        print(self.shipPositions)


def RunGame():
    playerBoard = GridBuilder('player', 'Blue', SIZE, NUMSHIPS)
    computerBoard = GridBuilder('Computer', 'Green', SIZE, NUMSHIPS)
    GridBuilder.printGrid(playerBoard)
    GridBuilder.printGrid(computerBoard)
    GridBuilder.PositionShips(playerBoard)

def main():
    print('-----Welcome to Battleship! Destroy the Enemy fleet!-----'.center(width))
    print('-----Empty sea is 0, ship loc is S, hit is *, miss is X-----\n'.center(width))
    RunGame()

main()