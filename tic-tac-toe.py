board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

#coords = {  '1 3': 0,'2 3': 1,'3 3': 2,
 #           '1 2': 3,'2 2': 4,'3 2': 5,
  #          '1 1': 6,'2 1': 7,'3 1': 8 }


game_still_going = True

winner = None

current_player = 'X'

columns = 3


def play_game():

    display_board()

    while game_still_going:

        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    if winner == 'X' or winner == 'O':
        print(winner, 'wins')
    elif winner == None:
        print('Draw')

def display_board():
    print('---------')
    print('|', board[0], board[1], board[2], '|')
    print('|', board[3], board[4], board[5], '|')
    print('|', board[6], board[7], board[8], '|')
    print('---------')

def handle_turn(player):
    #position = input('Enter the coordinates: ')
    #coord = position.split(' ')


    valid = False
    while not valid:
        position = input('Enter the coordinates: ')
        coord = position.split(' ')
        if coord[0].isnumeric() == False or coord[1].isnumeric() == False:
            print("You should enter numbers!")
            continue


        if int(coord[0]) < 1 or int(coord[0]) > 3 or int(coord[1]) < 1 or int(coord[1]) > 3:
            print('Coordinates should be from 1 to 3!')
            continue


        position = ((columns - (int(coord[1]) % columns)) % columns) * columns + (int(coord[0])-1)

        if board[position] == ' ':
            valid = True
        else:
            print('This cell is occupied! Choose another one!')
            continue
        board[position] = player


        display_board()



def check_if_game_over():
    check_for_winner()
    check_for_tie()

def check_for_winner():

    global winner

    row_winner = check_rows()

    column_winner = check_columns()

    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return

def check_rows():
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != ' '
    row_2 = board[3] == board[4] == board[5] != ' '
    row_3 = board[6] == board[7] == board[8] != ' '
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
    global game_still_going
    column_1 = board[0] == board[3] == board[6] != ' '
    column_2 = board[1] == board[4] == board[7] != ' '
    column_3 = board[2] == board[5] == board[8] != ' '
    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonals():
    global game_still_going
    diags_1 = board[0] == board[4] == board[8] != ' '
    diags_2 = board[2] == board[4] == board[6] != ' '
    if diags_1 or diags_2:
        game_still_going = False
    if diags_1:
        return board[0]
    elif diags_2:
        return board[2]
    return


def check_for_tie():
    global game_still_going
    if ' ' not in board:
        game_still_going = False
        return True
    else:
        return False

def flip_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'



play_game()
