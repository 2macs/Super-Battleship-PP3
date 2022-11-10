# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
import os
from subprocess import call

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
            # print(F'Rand row is {random_row}, random column is {random_col}')  
            # ensure ship location not already taken         
            if thisLoc not in self.shipPositions:
                self.shipPositions.append(thisLoc) 
                shipsPlaced += 1
        
        # draw the ships on the board
        for location in self.shipPositions:
           my_row = location[0]    
           my_col = location[1]    
           self.battleBoard[my_row][my_col] = 'S'
           # print(f'Row is {my_row}, col is {my_col}')   

    def add_guess(self, guess):
        """ Tke the guess from the player and the computer, add to guess list if a new guess //
        message the user to pick again if already guessed       """
            
        self.guesses.append(guess)
        print(f'Output form AddGuesses method is {self.guesses}')
        guess_row = int(guess[0])
        guess_col = int(guess[1])
        print(f'Guess breaks down to row {guess_row} and col {guess_col}')
        
        # check if guess is a hit or a miss
        if guess in self.shipPositions:
            self.score += 1
            self.battleBoard[guess_row][guess_col] = 'X'
            return 'HIT'
        else:
            self.battleBoard[guess_row][guess_col] = 'M'
            return 'MISS'
            

        
    def get_guess(self, my_name):
        guess = []
        
        if my_name == 'player':
            while True:
                try:
                    playerGuessRow = int(input('Enter a row number 0 - 5: '))
                except ValueError:
                    print('Entry must be a number')
                    continue

                if playerGuessRow >= 0 and playerGuessRow <= 5:
                    print(f'You entered: {playerGuessRow}')
                    break
                else:
                    print('The integer must be in the range 0-5')
                
            
            while True:
                try:
                    playerGuessCol = int(input('Enter a column number 0 - 5: '))
                except ValueError:
                    print('Entry must be a number')
                    continue

                if playerGuessCol >= 0 and playerGuessCol <= 5:
                    print(f'You entered: {playerGuessCol}')
                    break
                else:
                    print('The integer must be in the range 0-5')

            print(f'You guessed row {playerGuessRow} and column {playerGuessCol}')
            guess = [playerGuessRow, playerGuessCol]
            print(guess)
            return guess

        else:
            computerGuessRow = self.getRandomNumber(SIZE)
            computerGuessCol =  self.getRandomNumber(SIZE)
            print(f'Computer guessed row {computerGuessRow} and col {computerGuessCol}')
            guess = [computerGuessRow, computerGuessCol]
            print(guess)  
            return guess 


def welcomeMessage():
    print('-----Welcome to Battleship! Destroy the Enemy fleet!-----'.center(width))
    print('-----Empty sea is 0, ship loc is S, hit is X, miss is M-----\n'.center(width))


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
    while True:
        GridBuilder.printGrid(playerBoard)
        GridBuilder.printGrid(computerBoard)  
        playerGuess = GridBuilder.get_guess(playerBoard, 'player')
        playerResult = GridBuilder.add_guess(computerBoard, playerGuess)
        print(f'You scored a {playerResult}!')
        checkEndGame(playerBoard, computerBoard)
        computerGuess = GridBuilder.get_guess(computerBoard, 'computer')     
        computerResult = GridBuilder.add_guess(playerBoard, computerGuess)    
        print(f'You scored a {computerResult}!')
        print(f'Player score is {playerBoard.score}. Computer score is {computerBoard.score}')
        checkEndGame(playerBoard, computerBoard)


def checkEndGame(playerBoard, computerBoard):
    """ What happens when the end of the game is reached"""
    if playerBoard.score == NUMSHIPS: # All player ships are sunk
        print(f'Computer has hit all your ships ! You lose this one!')
        replay = input('Play again Y / N ?: ')
        if replay.upper() == 'Y':
            main()
        else:
            exit(-1)
    elif computerBoard.score == NUMSHIPS:
        print(f'You hit all the computer ships! You win!')
        replay = input('Play again Y / N ?: ')
        if replay.upper() == 'Y':
            main()
        else:
            exit(-1)
        

# Kick off game
main()