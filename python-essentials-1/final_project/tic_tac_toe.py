#!/usr/bin/env python3
#
# This is a simple program, which pretends to play 
# tic-tac-toe with the user.
#


from random import randrange



def display_board(board):
    """The function accepts one parameter containing the board's current status
    and prints it out to the console.
    
    """
    for row in board:
        print("+-------" * 3 + "+")
        print("|       " * 3 + "|")
        for field in row:
            print("|   " + str(field) + "   ", end="")
        print("|")
        print("|       " * 3 + "|")
    print("+-------" * 3 + "+")


def update_board(board, field, char):
    """Update the board at the given field of
    with the char.
    """

    row, column = get_field_coords(field)
    board[row][column] = char



# Dictionary with pairs of number and coordinates:
# num: (row, column)
# For use of get_field_coords() function.
coords = {}
n = 1
for row in range(3):
    for column in range(3):
        coords[n] = (row, column)
        n += 1


def get_field_coords(field: int):
    """Returns tuple of (row, column) coordinates
    for given num (from 1 to 9).
    
    """

    return coords[field]


def field_is_free(board, field):
    """Return True if field of the board is free (!= 'X' or 'O'),
    False otherwise.

    """

    free_fields = make_list_of_free_fields(board)
    if get_field_coords(field) in free_fields:
        return True
    else:
        return False


def enter_move(board):
    """The function accepts the board's current status, asks the user about their move, 
    checks the input, and updates the board according to the user's decision.

    """

    while True:
        field = input("Enter your move: ")
        try:
            field = int(field)
        except ValueError:
            print("It must be a number. Try again!")
            continue
        if field < 1 or field > 9:
            print("Number must be from 1 to 9. Try again!")
            continue
        elif not field_is_free(board, field):
            print("It must be not yet used. Try again!")
            continue
        else:
            break
    update_board(board, field, 'O')
    display_board(board)


def make_list_of_free_fields(board):
    """The function browses the board and builds a list of all the free squares; 
    the list consists of tuples, while each tuple is a pair of row and column numbers.

    """

    free_fields = []
    for row in board:
        for field in row:
            if field not in ["O", "X"]:
                free_field_coords = (board.index(row), row.index(field))
                free_fields.append(free_field_coords)

    return free_fields


def victory_for(board, sign):
    """The function analyzes the board's status in order to check if 
    the player using 'O's or 'X's has won the game.

    """
    is_victory = False
    
    # Check horizontally
    for row in board:
        if row == [sign, sign, sign]:
            is_victory = True
            break
    # Check vertically
    for n in range(3):
        column = [ row[n] for row in board ]
        if column == [sign, sign, sign]:
            is_victory = True
            break
    # Check diagonally
    if board[0][0] ==  board[1][1] == board[2][2] == sign or \
        board[0][2] == board[1][1] == board[2][0] == sign:
            is_victory = True

    return is_victory


def draw_move(board):
    """The function draws the computer's move and updates the board.

    """

    is_first_move = True
    for row in board:
        if "X" in row:
            is_first_move = False    
            break

    free_fields = make_list_of_free_fields(board)
    get_random_field = lambda: randrange(1, 10)
    
    
    if is_first_move:
        field = 5
    else:
        field = get_random_field()
        while get_field_coords(field) not in free_fields:
            field = get_random_field()

    update_board(board, field, "X")
    print('Computer moves:')
    display_board(board)
    

def main():
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    draw_move(board)
    counter = 1
    gameover = False

    while not gameover:
        if counter % 2 == 0:
            draw_move(board)
        else:
            enter_move(board)
        # Check, if the game is over
        if victory_for(board, 'X'):
            print("Computer wins. Sorry!")
            gameover = True
        elif victory_for(board, 'O'):
            print("You win! Congratulations!")
            gameover = True
        elif len(make_list_of_free_fields(board)) == 0:
            print("Nobody wins. A tie.")
            gameover = True
        counter += 1


if __name__ == "__main__":
    main()
