import random
import color


def check_if_won(copied_board, char):
    winning_chars = char+char+char
    copied_board = copied_board.replace('\n', '')
    for i in 0,3,6:
        if copied_board[i:i + 3] == winning_chars:
            return 1
    for i in range(3):
        if copied_board[i::3] == winning_chars:
            return 1
    if copied_board[0] + copied_board[5] + copied_board[8] == winning_chars:
        return 1
    elif copied_board[2] + copied_board[5] + copied_board[6] == winning_chars:
        return 1
    return 0


def coin_flip():
    if random.randint(1, 2) == 1:
        p = ['X', 'O']
    else:
        p = ['O', 'X']
    return p


def ai(board):
    board = board.replace('\n', '')
    return str(random.randint(1, 9))


def game(board):
    saved_board = board
    while True:
        won = False
        board = saved_board
        players = coin_flip()
        print('First Player is: ' + players[0])
        count = 0
        while not won and count != 9:
            for i in range(2):
                if count == 9:
                    print("It's a draw.")
                    break
                right = False
                turn = players[i]

                if i == 1:
                    while not right:
                        inp = ai(board)
                        if board.replace('\n', '')[int(inp) - 1] == inp:
                            board = board.replace(inp, turn)
                            print(inp)
                            right = True

                while not right:
                    inp = input('|' + color.tr_iter("|".join(board), 'XO', color.FgColor.Green) + "|\nIt's Player's '{}' turn. Type in the field:\n".format(turn))
                    if board.replace('\n', '')[int(inp) - 1] == inp:
                        board = board.replace(inp,turn)
                        right = True
                if check_if_won(board, turn) == 1:
                    print('{} has won!'.format(turn))
                    won = True
                    break
                count += 1
        if input('Wanna play again?') != 'yes':
            break


BOARD = '123\n456\n789'
game(BOARD)
