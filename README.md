![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# BattleShips ! 
This game is based on the famous battleships game that originated on paper, then migrated to boards and now to PC screens. In this version, a human player plays against the computer. Both players have a board , on the human player board the ship positions are printed to the screen while on the computer board the ship positions remain hidden to the human player. 
A ship is denoted on the board with an 'S', a hit on a ship is denoted with an 'X' while a miss is denoted with a 'M'. Empty sea / available guesses are denoted by '0' for the human player, all board locations for the computer are denoted with 'O' until there is either a hit or a miss. 
Ship positions for both players are randomly generated, each ship takes up one location on the board. 

### Screen at game startup
!['Intro screen'](assets/images/intro.PNG)



## Game Play
At start up the player is presented with 2 boards. The player board will show ship positions while the computer board will not. The player is then prompted to enter a row. The entry must be a number between 0 and 5. Once the player has entered a valid row number the player is then prompted to enter a column number number. The player guess is printed to the screen. The game then checks to see if the player has scored a hit or missed the computers ships and outputs the outcome to the screen in Green text. 
The computer then makes a random guess, the guess is printed to the screen and the game will check the computer's guess against the players ship positions and advise if the computer hit or missed the players ships. The computer result is printed in Red text. 

!['Game Play'](assets/images/first_choice.PNG)

The player is prompted to continue the game or not, if the player exitis then the game will print the current score and exit the game. Assuming the player selects 'Y' and continues , the game updates the boards with the hits / misses and reprints the boards at the top of the screen. The player is again prompted to enter a row / column until such tiome as the player exits or 5 ships have been destroyed for either player.

!['Game loop'](assets/images/game_loop.PNG)

On completion of the game, a message will print informing the player as to has won this time. 

!['Game win'](assets/images/game_win.PNG)

The game allows :
* Take user input and check to see if enemy ships are hit
* Play against a computer
* Provides feedback with respect to the ongoing score






* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!