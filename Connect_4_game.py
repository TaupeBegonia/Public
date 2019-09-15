#############################
#   Computer Project #7
#
#   Algorithm
#      Define start board, game board functions
#      Define color assignment function
#      Define board input function
#      Define winning sequence check functions
#      Define main function
#      Call main function
#          Display banner and instructions
#          Initialize game board, player colors
#          Alternate between players, update board for each turn
#              Check if disc is in a winning sequence
#                  Stop game if there is a win
#          Prompt to replay game
#      End program
#############################
pieces = {'black':'b', 'white':'w'} # dictionary of discs
COLUMN = 7 # constants
ROW = 6

def initialize():
    '''
    Creates an empty board of lists
    Return: empty board (list)
    '''
    board = [[0]*COLUMN for i in range(ROW)] # Creates a list of lists of 0s
    return board

def choose_color():
    '''
    Initializes player and opponent colors
    Return: player colors (str)
    '''
    game_color = input("Pick a color: ")
    # loops while wrong input
    while game_color.lower() != "black" and game_color.lower() != "white":
        print("Wrong color; enter only 'black' or 'white', try again.")
        game_color = input("Pick a color: ")
    if game_color.lower() == "black":
        play_color = "black"
        opp_color = "white"
    elif game_color.lower() == "white":
        play_color = "white"
        opp_color = "black"
    return play_color, opp_color # returns a tuple

def board_display(board):
    '''
    Created by Dr. Imen Zaabar as part of starting code
    Displays and updates game board
    board: the game board (list)
    Return: no return
    '''
    print("Current board:")
    C = COLUMN
    R = ROW
    hline = '\n' + (' ' * 2) + ('+---' * C) + '+' + '\n'
    numline = ' '.join([(' ' + str(i) + ' ') \
                        for i in range(1, C + 1)])
    str_ = (' ' * 3) + numline + hline
    for r in range(0, R):
        str_ += str(r+1) + ' |'
        for c in range(0, C):
            str_ += ' ' + \
                (str(board[r][c]) \
                     if board[r][c] is not 0 else ' ') + ' |'
        str_ += hline
    print (str_) # Draws out board

def drop_disc(board, column, color): 
    '''
    Places a disc on the 'board' by replacing a 0
    board: the game board (list)
    column: column to drop disc by player input (int)
    color: current player's color (str)
    Return: the modified row on board (int)
        if invalid column, return None (NoneType)
        if column full, return 'full' (str)
    '''
    if column < 1 or column > 7: # if invalid column input
        return None
    col_in = column - 1 # subtract 1 to match index
    count = 0 # start loop counter at 0
    for game in board[::-1]: # checks bottom row first
        count += 1
        if game[col_in] == 0:
            game[col_in] = pieces[color] # assigns disc based on dictionary key
            count -= 1
            # the modified row, or (# of rows - # times looped)
            return ROW - count
    else: # if column is full
        return 'full'

def check_disc(board, row, column):
    '''
    Checks board for a winning sequence given a board location
    board: the game board (list)
    row: the modified row from drop_disc() (int)
    column: column to drop disc by player input (int)
    Return: if winning sequence found, True (bool)
        if none found, False (bool)
    '''
    col_in = column - 1 # subtract 1 to account for index
    row_in = row - 1
    if col_in < 0 or col_in > 6: # if column and row not in range
        return None
    if row_in < 0 or row_in > 5:
        return None
    # for horizonatal wins
    for n in range(4): 
        if board[row_in][n] == board[row_in][n + 1] == \
            board[row_in][n + 2] == board[row_in][n + 3] and \
            board[row_in][n] != 0:
            # if there are 4 consecutives of same disc and not 0s
            if (row_in,col_in) == (row_in, n) or \
                (row_in, col_in) == (row_in, n + 1) or \
                (row_in, col_in) == (row_in, n + 2) or \
                (row_in, col_in) == (row_in, n + 3): # compares tuples if 
                                            # point among winning sequence
                return True
    # for vertical wins
    for cols in range(col_in, col_in + 1): # checks the given column
        for n in range(3): # limited range so index will not be out of range
            if board[n][cols] == board[n + 1][cols] == board[n + 2][cols] == \
                board[n + 3][cols] and board[n][cols] != 0:
                if (row_in, col_in) == (n, cols) or \
                    (row_in, col_in) == (n + 1, cols) or \
                    (row_in, col_in) == (n + 2, cols) or \
                    (row_in, col_in) == (n + 3, cols):
                    return True
    # for downsloping diagonal wins, checks for wins from upper-left corner
    for x in range(3):
        for y in range(4):
            if board[x][y] == board[x + 1][y + 1] == board[x + 2][y + 2] == \
                board[x + 3][y + 3] and board[x][y] != 0:
                if (row_in, col_in) == (x, y) or \
                    (row_in, col_in) == (x + 1, y + 1) or \
                    (row_in, col_in) == (x + 2, y + 2) or \
                    (row_in, col_in) == (x + 3, y + 3):
                    return True
    # for upsloping diagonal wins, checks for wins from upper-right corner
    for x in range(3):
        for y in range(6,2,-1):
            if board[x][y] == board[x + 1][y - 1] == board[x + 2][y - 2] == \
                board[x + 3][y - 3] and board[x][y] != 0:
                if (row_in, col_in) == (x, y) or \
                    (row_in, col_in) == (x + 1, y - 1) or \
                    (row_in, col_in) == (x + 2, y - 2) or \
                    (row_in, col_in) == (x + 3, y - 3):
                    return True

    return False # if no wins found
def is_game_over(board):
    '''
    Calls check_disc() to each board spot to find if winner exists
    board: the game board (list)
    Return: if check_disc is True, return disc color (str)
        if board is full, return 'draw' (str)
        if neither, return None (NoneType)
    '''
    is_full = True # set initial condition
    for row in range(6): # for all rows
        for col in range(7): # for all columns
            if board[row][col] == 0:
                is_full = False # change variable to false, so return is None
            # add 1 as check_disc() subtracts 1
            elif check_disc(board, row + 1, col + 1):
                if board[row][col] == "b":
                    return 'black'
                elif board[row][col] == "w":
                    return 'white'
            
    if is_full: # when no 0s or wins found
        return 'draw'
    else:
        return None
    
def main():
    '''
    Plays Connect4 with player interaction
    Return: no return
    '''
    banner = """
       ____ ___  _   _ _   _ _____ ____ _____ _  _   
      / ___/ _ \| \ | | \ | | ____/ ___|_   _| || |  
     | |  | | | |  \| |  \| |  _|| |     | | | || |_ 
     | |__| |_| | |\  | |\  | |__| |___  | | |__   _|
      \____\___/|_| \_|_| \_|_____\____| |_|    |_|  
    """
    intro = """
    Connect Four is a two-player connection game in which the players first choose a color and \
    then take turns dropping one colored disc from the top into a seven-column, six-row vertically suspended grid. \
    The pieces fall straight down, occupying the lowest available space within the column. \
    The objective of the game is to be the first to form a horizontal, vertical, or diagonal line of four of one's own discs. 
    """
    usage = """
        Usage:
            pass:   give up, admit defeat
            exit:   exit the game
            i:      drop a disk into column i
    """
    print(banner)
    print(intro)
    print(usage)
     
    continue_game = 'yes'  # can't use "continue" because it has a special 
                            # meaning
    while continue_game == 'yes':
        play_num = 0 # set player alternator to 0
        game_board = initialize() # create game board
        game_colors = choose_color() # determine player colors
        print("You are '{}' and your opponent is '{}'.".format(game_colors[0],\
              game_colors[1]))
        board_display(game_board) # display board
        while True:
            if play_num % 2 == 0: # main player color assignment
                player = game_colors[0]
                opp = game_colors[1]
            else: # opponent color assignment
                player = game_colors[1]
                opp = game_colors[0]
            play_input = input("{}'s turn :> ".format(player))
            # loops while invalid input
            while play_input != "pass" and play_input != "exit" and \
                play_input.isdigit() == False:
                print("Invalid option")
                print(usage)
                play_input = input("{}'s turn :> ".format(player))
            if play_input == "pass":
                print("{} gave up!".format(player)\
                      +" {} is the winner!! yay!!!".format(opp))
                break # stops playing game
            if play_input == "exit":
                print("\nThanks for playing! See you again soon!")
                break
            board_in = int(play_input)
            board_out = drop_disc(game_board, board_in, player)
            # puts in disc based on column input, returns modified row
            if board_out == None or board_out == "full": # for invalid inputs
                if board_out == None:
                    print("Invalid column: 1 <= column <= 7. "\
                          +"Please try again.")
                elif board_out == "full":
                    print("This column is full. Please try again.")
                continue # go back to prompting input
            board_display(game_board)
            play_num += 1 # change turns by changing even/odd number
            winner = is_game_over(game_board) # checks for win
            if winner == "draw" or winner == "black" or winner == "white":
                if winner == "draw":
                    print("The board is full so this game ends in a draw.")
                elif winner == "black" or winner == "white":
                    print("{} wins!".format(winner))
                break
        if play_input == "exit":
            break # breaks out of topmost while loop to avoid question
        continue_game = input("Would you like to play again? ").lower() 
    else:
        print("\nThanks for playing! See you again soon!")
    
if __name__ == "__main__":
    main()