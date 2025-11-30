import random

""" Pseudocode 
        Prompt user input for total rounds of the game
        Initialize the total game score
        for each round:
            Validate the user input for board size and number of ships
            Handle invalid entries 
            Set the board and ships.
            for each shot in the round:
                Request the user to input the assumed ship coordinates
                Display the Hit message (Hit or Miss)
                Display the full board with updated attempts results 
            Show the final state of the board
            Display the user final score of this round
        Display the user final score of the game
"""

""" Import the libraries if appliable
"""

""" Define global variables if appliable
"""


# CurrentRound
# Flag
# totalscore
# board

def createBoard(size):
    """ Function Description:
            Creates a size-by-size game board initialized with '~'
        Parameter(s):
            size [int]: The size of the board which will be used to create a board of size x size
                        Example: size 2 will create [ ['~', '~'], ['~', '~']]
        Return: board which is a list of lists
    """
    board = []
    for row in range(size):
        newBoard = []
        for column in range(size):
            newBoard.append('~')  # represents blanks/water
        board.append(newBoard)
    return board


# import battleShip as ship
# board = createBoard(5)
# print(board)

def addShip(board, numShips):
    """ Function Description:
            Randomly places the specified number of ships ('S') on the board.
        Parameter(s):
            board : The list of lists representing the game board
            numShips [int]: The number of ships that user wants on the board
        Return: None
    """
    size = len(board)
    ships_placed = 0
    # Places ships until the required number is reached
    while ships_placed < numShips:
        # Randomly slects a row and column coordinate for a ship
        row = random.randint(0, size - 1)
        column = random.randint(0, size - 1)
        # Place ship if index is empty('~')
        if board[row][column] == '~':
            board[row][column] = 'S'  # 'S' is a ship
            ships_placed += 1  # Increment the count of placed ships
    return None


# import battleShip as ship
# board = ship.create(5)
# ship.addShip(board, 4)
# print(board)

def checkSetUpError(size, numShips):
    """ Function Description:
            Validates user input for the size of the board and the number of ships.
        Parameter(s):
            size [int]: The size of the board
            numShips [int]: The number of ships
        Return [Boolean]: Return True if an error is found or False if there is no error.
    """
    # checks that board size is within valid range( 2x2 - 5x5)
    if size < 2:
        return True
    elif size > 5:
        return True
    # maximum amount of ships on the board
    shipmax = (size * size) - 2
    # Ensures ships are within the valid range
    if numShips < 1:
        return True
    elif numShips > shipmax:
        return True

    return False


# import battleShip as ship
# ship.checkSetUpError(5, 5)
# False
# ship.checkSetUpError(1, 5)
# True
# ship.checkSetUpError(2, 5)
# True
# ship.checkSetUpError(2, 2)
# False

def displayBoard(board, round=True):
    """ Function Description:
            Displays the current state of the board.  If round is True then print out the current
            state of the board without showing the ships 'S'.  Else round is False then print out the
            current state of the board showing hits 'X', misses 'O', ships that have not been hit 'S'
            and everything else '~'.
        Parameter(s):
            board : The list of lists representing the game board.
            round [Boolean] : True if you are print the board after each shot and False to display
            the end of a round version.  Default value of True.

        Return: None
    """
    size = len(board)
    for row in range(size):
        for column in range(size):
            i = board[row][column]
            if round:
                # When round=True: Hides ship('S') and only displays hits('X') or misses('O')
                if i == 'S':
                    print('~', end=' ')
                elif i == 'X':
                    print('X', end=' ')
                elif i == 'O':
                    print('O', end=' ')
                else:
                    print('~', end=' ')
            else:
                # When round=False: displays board with ship locations
                if i == 'X':
                    print('X', end=' ')
                elif i == 'O':
                    print('O', end=' ')
                elif i == 'S':
                    print('S', end=' ')
                else:
                    print('~', end=' ')
        print()

    print()
    return None


# import battleShip as ship
# board = ship.createBoard(5)
# ship.addShip(board, 3)
# ship.displayBoard(board)
# ship.displayBoard(board, False)

def fireShot(board, row, column):
    """ Function Description:
            Marks a shot on the board.
        Parameter(s):
            board : The list of lists representing the game board
            row [int]: The row coordinate entered by the user.
            col [int]: The col coordinate entered by the user.
        Return[Boolean]: Return True if a ship was hit and False if the shot missed a ship.
    """
    if board[row][column] == 'S':
        board[row][column] = 'X'  # Hit if coordinates are where ships are located
        return True
    elif board[row][column] == '~':
        board[row][column] = 'O'  # Miss if no ships are on coordinates
        return False
    return False


# import battleShip as ship
# board = ship.createBoard(5)
# ship.addShip(board, 3)
# ship.displayBoard(board, False)
# ship.fireShot(board, int, int)
# ship.displayBoard(board)

def checkFireError(board, row, column):
    """ Function Description:
            Validates user input for the coordinates to shot a ship
        Parameter(s):
            board : The list of lists representing the game board
            row [int]: The row coordinate entered by the user.
            col [int]: The col coordinate entered by the user.
        Return [Boolean]: Return True if an error is found or False if there is no error.
    """
    size = len(board)
    # checks if coordiantes are within board boundaries
    if row < 0 or row >= size or column < 0 or column >= size:
        return True
    # checks if index is already hit or missed
    if board[row][column] == 'X' or board[row][column] == 'O':
        return True
    return False


# import battleShip as ship
# board = ship.createBoard(5)
# ship.addShip(board, 3)
# ship.displayBoard(board, False)
# ship.checkFireError(board, int, int)
# ship.fireShot(board, int, int)

def playRound(board, numShips):
    """ Function Description:
            Main logic for playing one round

            Pseudocode:
            Keep track of number of shots for the round
            Keep track of the score (number of hits) for the round
            Loop until user fires all their shots
                Ask user to enter coordinates for their shot.  Input two numbers separated by a space.
                Validate the shot coordinates using checkFireError function
                Fire a shot using the fireShot function
                Output if the shot is a hit or a miss
                display the board after the shot has been taken displayBoard(board)
            Output "End of round X"
            display the board at the end of the round displayBoard(board, False)

        Parameter(s):
            board : The list of lists representing the game board
            numShips [int]: The number of ships
        Return [int]: The number of hits (ships that were hit) for the round.
    """
    size = len(board)
    remainderShots = numShips  # number of round = number of ships
    numHits = 0  # Tracks hits on ships
    shotcounter = 0  # count total shot for the round
    while remainderShots > 0:
        # Prompts player to enter coordinates for a shot
        player = input("Enter row and column to take a shot (e.g 2 3): ")
        row, column = map(int, player.split())
        # checks if the coordinate is valid
        if checkFireError(board, row, column):
            print("You willl need to enter a valid coordinates.")
            continue
        # Updates shot whether a hit or a miss
        elif fireShot(board, row, column):
            shotcounter += 1
            print(f"Shot {shotcounter} is a Hit!")
            numHits += 1
            displayBoard(board, round=True)
        else:
            shotcounter += 1
            print(f"Shot {shotcounter} is a Miss!")
            displayBoard(board, round=True)

        remainderShots -= 1  # Decrement remaing shots
    print("End of round:")
    print("")
    displayBoard(board, round=False)

    return numHits


# import battleShip as ship
# board = ship.createBoard(5)
# ship.addShip(board, 3)
# ship.displayBoard(board, False)
# ship.playRound(board, 3)

def main():
    """ Function Description:
            Play the game in a designated number of rounds and present the final score to the user.
            You can not change the code in the main function.  If student changes the main function code
            then they will lose 25 marks.
        Parameter(s): No parameters
        Return: None
    """
    currentRound = 0
    numRounds = int(input("Enter the number of rounds of Battleship you want to play: "))
    flag = True
    while currentRound < numRounds:
        while flag:
            size = int(input("Enter the size of the board: "))
            numShips = int(input("Enter the number of ships: "))
            flag = checkSetUpError(size, numShips)
            if (flag == False):
                break
            else:
                print("You will need to enter the size of the board and number of ships again.")

        board = createBoard(size)
        addShip(board, numShips)
        print(f"\nRound {currentRound + 1}:\n")
        hits = playRound(board, numShips)
        totalScore = 0
        totalScore += hits
        currentRound += 1
    print(f"\nFinal Score after {numRounds} round(s) is {totalScore} out {numShips * numRounds}.")
    return


if __name__ == '__main__':
    main()