import random
from os import system, name
from time import sleep

# Initialize Global Variables
game_on = True
game_list = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
board = {'a1': ' ', 'a2': ' ', 'a3': ' ', 'b1': ' ',
         'b2': ' ', 'b3': ' ', 'c1': ' ', 'c2': ' ', 'c3': ' '}
current_player = 1
comp_move = ''


def reset_game():
    # This function resets all of the global variables to their original setting

    # Declares all Global Variables
    global game_list
    global board
    global current_player
    global comp_move

    # Resets all Global Variables
    game_list = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
    board = {'a1': ' ', 'a2': ' ', 'a3': ' ', 'b1': ' ',
             'b2': ' ', 'b3': ' ', 'c1': ' ', 'c2': ' ', 'c3': ' '}
    current_player = 1
    comp_move = ''


def display_board(board):
    # BOARD DISPLAY EXAMPLE
    #
    #       |   |
    # 3   X | O |
    #    ___|___|___
    #       |   |
    # 2   O | X |
    #    ___|___|___
    #       |   |
    # 1   O |   | X
    #       |   |
    #     a   b   c

    # Setup board and choice selection to mimic making moves in chess

    print('     |   |   ')
    print('3  ' + board.get('a3') + ' | ' +
          board.get('b3') + ' | ' + board.get('c3') + ' ')
    print('  ___|___|___')
    print('     |   |   ')
    print('2  ' + board.get('a2') + ' | ' +
          board.get('b2') + ' | ' + board.get('c2') + ' ')
    print('  ___|___|___')
    print('     |   |   ')
    print('1  ' + board.get('a1') + ' | ' +
          board.get('b1') + ' | ' + board.get('c1') + ' ')
    print('     |   |   ')
    print('   a   b   c ')


def clear():
    # Clears screen for windows, linux, and mac

    # Clears for Windows
    if name == 'nt':
        _ = system('cls')

    # Clears for mac and linux
    else:
        _ = system('clear')


def position_choice(player):
    # This function asks the player where they want to move and then updates the board

    # GLOBAL Variables
    global game_list
    global board
    global current_player

    # LOCAL Variables
    valid_choice = False
    choice = ''
    count = 0

    # Checks user move choice
    while not valid_choice:
        choice = input(
            f'Player {current_player}, choose a position by typing the row and column (i.e. a1, b3, c2): ')
        if choice in game_list:
            valid_choice = True
        else:
            print('Sorry, invalid choice!')

    # Updates the board with the player's choice "X" or "O"|
    board[choice] = player

    # Removes the player choice from the list of available choices
    for x in game_list:
        if choice == x:
            game_list.pop(count)
            break
        else:
            count += 1


def gameon_choice(x):
    # Once the game ends, this function is called asking if the Player wants to play again

    # LOCAL variables
    continue_playing = ['Yes', 'No',]
    result = ''
    continue_check = False

    # Checks if the user wishes to play the game again
    while not continue_check:
        result = input('Do you want to play again? Enter Yes or No: ')
        if result in continue_playing:
            if result == 'Yes':
                x = True
            else:
                x = False
            continue_check = True
        else:
            print('Sorry, invalid choice!')
    return x


def gameover_check(game_list, board):
    # Check if game board is full, and if not will check if there is a winning move
    if not game_list:
        return True
    else:
        return victory_check(board)


def victory_check(board):
    # Checks if victory by going through all eight possible win conditions. First checks
    # if the first value is not blank, then checks if other values to secure win are
    # the same as the first value.
    if board['a1'] != " " and board['a1'] == board['a2'] and board['a1'] == board['a3']:
        return True
    elif board['b1'] != " " and board['b1'] == board['b2'] and board['b1'] == board['b3']:
        return True
    elif board['c1'] != " " and board['c1'] == board['c2'] and board['c1'] == board['c3']:
        return True
    elif board['a1'] != " " and board['a1'] == board['b1'] and board['a1'] == board['c1']:
        return True
    elif board['a2'] != " " and board['a2'] == board['b2'] and board['a2'] == board['c2']:
        return True
    elif board['a3'] != " " and board['a3'] == board['b3'] and board['a3'] == board['c3']:
        return True
    elif board['a1'] != " " and board['a1'] == board['b2'] and board['a1'] == board['c3']:
        return True
    elif board['a3'] != " " and board['a3'] == board['b2'] and board['a3'] == board['c1']:
        return True
    else:
        return False


def switch_player(player):
    # This function switches between Player 1 and the computer
    if player == 1:
        player = 2
    else:
        player = 1
    return player


def computer_move():
    # This function sets up how the computer decides its move.
    # The computer will first check if the next move will result in computer win. If yes, will pick this option.
    # If not satisfied, the computer will then check if the player's next move will result in computer defeat. Computer will choose this option
    # If neither victory nor defeat, the computer will see if any corners are available and take it.
    # If no corners are available, the computer will choose the center position.
    # If none of the above criteria are met, the computer will choose any random position.

    # Define GLOBAL Variables
    global board
    global comp_move
    global game_list

    # Define LOCAL Variable
    count = 0
    move_found = False

    # Clear comp_move of the previous move
    comp_move = ''

    # This is the computer moves
    while not move_found:
        # Computer will check if it's move will cause it to win
        if check_comp_win(game_list, board):
            move_found = True
            break

         # Computer will check if the player's next move will cause the computer to lose.
         # Computer will block the move causing the player's win if true.
        elif block_player(game_list, board):
            move_found = True
            break

        # Will check if any corners are available for the computer to take
        elif take_corner(game_list):
            move_found = True
            break

        # If no corners are available, will check if the center is available and take it
        elif take_center(game_list):
            move_found = True
            break

        # If the corners and center are not available, the computer will take any available space
        elif take_any(game_list):
            move_found = True
            break

    # Computer move here
    board[comp_move] = 'O'

    # Remove comp move from list of open spaces
    for x in game_list:
        if x == comp_move:
            game_list.pop(count)
            break
        else:
            count += 1


def check_comp_win(game_list, board):
    # This function determines if the computer's next move will result in a win.

    # Define GLOBAL Variable
    global comp_move

    # Cycle through all available moves the computer can make and determine if a win
    for x in game_list:
        board[x] = 'O'

        # If victory, sets the computers move and returns true.
        # If not reset the board space and continue for all remaining options.
        if victory_check(board):
            comp_move = x
            return True
        else:
            board[x] = ' '
    return False


def block_player(game_list, board):
    # This function determines if the player is one move away from winning. This is used so the computer can prevent this outcome.

    # Define GLOBAL Variable
    global comp_move

    # Cycle through all available moves the player can make in the next turn
    # Will determine a computer loss
    for x in game_list:
        board[x] = 'X'

        # If victory, sets the computers move and returns true. This will block the Player from having a win.
        # If not reset the board space and continue for all remaining options.
        if victory_check(board):
            comp_move = x
            return True
        else:
            board[x] = ' '
    return False


def take_corner(game_list):
    # This function determines if a corner is available and chooses one at random.

    # Define GLOBAL Variable
    global comp_move

    # Define LOCAL Variable
    temp_list = []

    # Computer determines if a corner is available and chooses it
    for x in game_list:
        if x == 'a1' or x == 'a3' or x == 'c1' or x == 'c3':
            temp_list.append(x)

    # Checks if any of the corners are available. If yes, will select the first one in the shuffled list
    if len(temp_list) == 0:
        return False
    else:
        random.shuffle(temp_list)
        comp_move = temp_list[0]
        return True


def take_center(game_list):
    # The computer determines if the center is available and chooses the center

    # Define GLOBAL Variable
    global comp_move

    # Checks if the center ('b2') is in the list of available moves
    if 'b2' in game_list:
        comp_move = 'b2'
        return True
    else:
        return False


def take_any(game_list):
    # Function randomly sorts the remaining spaces and chooses the first one in the random list

    # Define GLOBAL Variable
    global comp_move

    # Randomize the game_list to grab a random corner for the computer to choose
    random.shuffle(game_list)

    # Computer determines if a corner is available and chooses it
    for x in game_list:
        comp_move = x
        return True

# Player 1 = 'X' and Computer = 'O'


# Resets the game values and displays the current board
reset_game()
clear()
display_board(board)
game_on = True  # Allows someone to restart the game

# Loop to continue the game
while game_on:
    # Checks the player move and updates the board
    if current_player == 1:
        position_choice('X')
    else:
        # Have run Computer here
        sleep(2)
        computer_move()

    clear()
    display_board(board)

    # Checks if the game is over and if the game is over will output if Tie or Winner
    if gameover_check(game_list, board):
        if victory_check(board) and current_player == 1:
            print(f"Congratulations! Player {current_player} is the Winner!")
        elif victory_check(board) and current_player == 2:
            print(f"The computer has won! Player 1 has been defeated!")
        else:
            print("The game ended in a Tie")

        reset_game()  # resets the game board variables
        # Checks at the end of the game if the user wishes to continue playing
        game_on = gameon_choice(game_on)
        # This will always make Player 1 start first
        current_player = switch_player(current_player)

        # If playing again will display the new board
        if game_on:
            clear()
            display_board(board)
        else:
            print('Thank you for playing!')

    # Switches the player turn to the next player
    current_player = switch_player(current_player)
