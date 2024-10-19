
def print_board(board: list[list[str]]) -> None:
    for row in board:
        print(*row)

#返り値はどうしたらよいか。。。。
#型は何の指定をしたらよいか。
def turn():
    print("xxxxのターンです")
    print("行0-2を入力してください")
    row = int(input())
    print("列0-2を入力してください")
    column = int(input())
    return row, column


#したいこと、
# print_bord関数で現在の盤面を表示
# turn関数で行列入力を受け付ける→return で受け付けたrow,columnを返り値にする
# 交互に行って９回まで行う。
#for _ in range(9):


def main():
    player1 = "◯"
    player2 = "✗"

    game_board = [["-" for _ in range(3)] for _ in range(3)]
    print_board(board=game_board)

    #for _ in range(9):
    
    turn()
    game_board[row][column] = player1
#UnboundLocalError: cannot access local variable 'row' where it is not associated with a value
#rowにあくせすできません。→グローバル変数ではなく、範囲外だからではないか？
    print("player2のターンです")
    print("行0-2を入力してください")
    row = int(input())
    print("列0-2を入力してください")
    column = int(input())
    game_board[row][column] = player2

    print_board(board=game_board)

   


if __name__ == '__main__':
    main()
