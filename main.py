board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
coordinates = ['00', '01', '02', '10', '11', '12', '20', '21', '22']
player = 'x'
win = False
step = 0

def current_player():
    global player
    if player == 'x':
        player = 'o'
    else:
        player = 'x'


def check_win():
    global win
    global player
    if board[0] == board[1] and board[1] == board[2] and board[2] != '-':  # горизонтальные
        win = True
        player = board[0]
        return win
    elif board[3] == board[4] and board[4] == board[5] and board[5] != '-':
        win = True
        player = board[3]
        return win
    elif board[6] == board[7] and board[7] == board[8] and board[8] != '-':
        win = True
        player = board[6]
        return win
    elif board[0] == board[3] and board[3] == board[6] and board[6] != '-':  # вертикальные
        win = True
        player = board[0]
        return win
    elif board[1] == board[4] and board[4] == board[7] and board[7] != '-':
        win = True
        player = board[1]
        return win
    elif board[2] == board[5] and board[5] == board[8] and board[8] != '-':
        win = True
        player = board[2]
        return win
    elif board[0] == board[4] and board[4] == board[8] and board[8] != '-':  # диагональные
        win = True
        player = board[0]
        return win
    elif board[2] == board[4] and board[4] == board[6] and board[6] != '-':
        win = True
        player = board[2]
        return win
    else:
        return


def player_step():
    global player
    count = 0
    player_coordinates = input('Введите координаты: ')
    while player_coordinates not in coordinates:
        print(f'{player_coordinates} не подходит. Пишите 01, 21, 20 и т.п.')
        player_coordinates = input('Введите координаты: ')
    while True:
        for i in coordinates:
            if i == player_coordinates:
                board[count] = player
                return False
            else:
                count += 1




def board_print():
    print(' ' + ' 0' + ' 1' + ' 2')
    print(
        f'0 {board[0]} {board[1]} {board[2]} \n1 {board[3]} {board[4]} {board[5]} \n2 {board[6]} {board[7]} {board[8]}')


def start_game():
    global step
    global win
    while win == False:
        if step < 9:
            step += 1
            print('Крестики-нолики')
            print(f'Ход №{step}')
            board_print()
            print(f'Ходит игрок {player}')
            player_step()
            current_player()
            check_win()
            print('_______________')
            start_game()
        else:
            print('Ничья!')
            break

    board_print()
    print(f'Победил игрок {player}')


start_game()
