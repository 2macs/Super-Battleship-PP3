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
        self.guesses = []     
        self.score = 0 
        

    def printGrid(self):
        """ Build and print the computer and player grids"""
        print(f'{self.name} grid'.center(width))
        for row in self.battleBoard:
            print("".join(row).center(width))
        print('\n')
    
    def getRandomNumber(self, SIZE):
        """ Generate a random number and return it"""
        Size = SIZE
        return random.randint(0,Size - 1)

    def PositionShips(self):
        """ Randomly locate NUMSHIPS of ships on the board"""
        shipsPlaced = 0 
        while shipsPlaced < NUMSHIPS:
            random_row = self.getRandomNumber(SIZE)
            random_col = self.getRandomNumber(SIZE)
            thisLoc = [random_row,random_col]
            print(F'Rand row is {random_row}, random column is {random_col}')  
            # ensure ship location not already taken         
            if thisLoc not in self.shipPositions:
                self.shipPositions.append(thisLoc) 
                shipsPlaced += 1
        
        # draw the ships on the board
        for location in self.shipPositions:
           my_row = location[0]    
           my_col = location[1]    
           self.battleBoard[my_row][my_col] = 'S'
           print(f'Row is {my_row}, col is {my_col}')   
    
    def get_guess(self, my_name):
        guess = []
        
        if my_name == 'player':
            playerGuessRow = input('Enter a row number 1 - 6: ')
            playerGuessCol = input('Enter a column number 1 - 6: ')
            print(f'You guessed row {playerGuessRow} and column {playerGuessCol}')
            guess = [playerGuessRow, playerGuessCol]
            print(guess)
        else:
            computerGuessRow = self.getRandomNumber(SIZE)
            computerGuessCol =  self.getRandomNumber(SIZE)
            print(f'Computer guessed row {computerGuessRow} and col {computerGuessCol}')
            guess = [computerGuessRow, computerGuessCol]
            print(guess)




           
        # print(f'{self.name} ship locs are {self.shipPositions}') 
        # print(self.battleBoard)
            

def welcomeMessage():
    print('-----Welcome to Battleship! Destroy the Enemy fleet!-----'.center(width))
    print('-----Empty sea is 0, ship loc is S, hit is *, miss is X-----\n'.center(width))

def main():
    """    Print welcome message, initialise boards, start game
    """
    welcomeMessage()   
    # Build initial board
    playerBoard = GridBuilder('player', 'Blue', SIZE, NUMSHIPS)
    computerBoard = GridBuilder('Computer', 'Green', SIZE, NUMSHIPS)      
    # Position ships on player board and computer board
    GridBuilder.PositionShips(playerBoard)
    GridBuilder.PositionShips(computerBoard)
    playGame(playerBoard, computerBoard)

def playGame(playerBoard, computerBoard):
    """ Controls the game loop"""
    GridBuilder.printGrid(playerBoard)
    GridBuilder.printGrid(computerBoard)  
    GridBuilder.get_guess(playerBoard, 'player')
    GridBuilder.get_guess(computerBoard,'computer')
    
    
    
main()