
# 返り値はNoneで、出力のみを行う。
def print_board(board: list[list[str]]) -> None:
    for row in board:
        print(*row)

def set_stone(p,game_board):
    try:
        print(f"{p}のターンです")
        print("行0-2を入力してください")
        row = int(input())
        print("列0-2を入力してください")
        column = int(input())
        game_board[row][column] = p
        print_board(board = game_board)
        if p == "◯":
            p = "×"
        else:
            p = "◯"

        return p, game_board
    except ValueError:
        print("0-2の数字を入力してください")
    except IndexError:
        print("盤外を選択されました")


def main():
    game_board = [["-" for _ in range(3)] for _ in range(3)]
    print_board(board = game_board)
    for turn in range(9):
            if turn % 2 == 0:
                player = "◯"
                set_stone(p = player, game_board = game_board)
            else:
                player = "×"
                set_stone(p = player, game_board = game_board)
            game_winner(game_board)

def game_winner(game_board):
    if "-" not in game_board[0][0] and game_board[0][0] == game_board[0][1] == game_board[0][2] \
    or \
    "-" not in game_board[1][0] and game_board[1][0] == game_board[1][1] == game_board[1][2] \
    or \
    "-" not in game_board[2][0] and game_board[2][0] == game_board[2][1] == game_board[2][2] \
    or \
    "-" not in game_board[0][0] and game_board[0][0] == game_board[1][1] == game_board[2][2] \
    or \
    "-" not in game_board[0][0] and game_board[0][0] == game_board[1][0] == game_board[2][0] \
    or \
    "-" not in game_board[0][1] and game_board[0][1] == game_board[1][1] == game_board[2][1] \
    or \
    "-" not in game_board[0][2] and game_board[0][2] == game_board[1][2] == game_board[2][2] \
    or \
    "-" not in game_board[0][0] and game_board[0][0] == game_board[1][1] == game_board[2][2] \
    or \
    "-" not in game_board[2][0] and game_board[2][0] == game_board[1][1] == game_board[0][2]:
        print("WIN")


    # for turn in range(9):
    #     set_stone(p = player1)
    #     print_board(board=game_board)
    #     # playerを交代させる


if __name__ == '__main__':
    main()
