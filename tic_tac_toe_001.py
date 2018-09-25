import random
board = [' ' for space in range(10)]


def space_check(pos):
    return board[pos] == ' '


def full_board():
    return  ' ' not in board



def win_check(sym):
    if board[1] + board[5] + board[9] == sym*3:
        return True
    elif board[7] + board[5] + board[3] == sym*3:
        return True
    elif board[1] + board[2] + board[3] == sym*3:
        return True
    elif board[8] + board[5] + board[2] == sym*3:
        return True
    elif board[4] + board[5] + board[6] == sym*3:
        return True
    elif board[7] + board[8] + board[9] == sym*3:
        return True
    elif board[1] + board[4] + board[7] == sym*3:
        return True
    elif board[9] + board[6] + board[3] == sym*3:
        return True
    else:
        return False


def display_board():
    """
    displays the game board
    """
    global board
    print(f'\n {board[7]} | {board[8]} | {board[9]}')
    print('___|___|___')
    print(f' {board[4]} | {board[5]} | {board[6]}')
    print('___|___|___')
    print(f' {board[1]} | {board[2]} | {board[3]}')
    print('___|___|___')


def place_marker(marker, place):
    global board
    board[place] = marker


def player_input():
    """
    returns a list of players symbols 
    """
    choice = ' '
    while choice.upper() not in ['X', 'O']:
        choice = input('Player 1 would you like to be X or O?: ')
    if choice == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']



print('\nHello, welcome to yet another tic-tac-toe game!')
while True:
    board = [' ' for space in range(10)]
    board[0] = '#'
    play_game = True
    players = player_input()
    cp = random.randint(0,1) # current player
    
    while play_game:
        display_board()
        print(f'{players[cp]} it is your turn')
        space = 0
        while not space_check(int(space)):
            space = input('Please choose a space 1-9: ')
            if not space.isdigit() or int(space) not in range(10):
                space = 0
        board[int(space)] = players[cp]
        if win_check(players[cp]):
            print(f'{players[cp]} wins!')
            play_game = False
        elif full_board():
            print('The game is a draw')
            play_game = False
        cp = (cp + 1 )% 2
    replay = input("Would you like to play again (Y)es (N)o: ")
    if replay.upper() != 'Y':
        break
print("thank you for playing!")



