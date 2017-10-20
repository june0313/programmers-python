def findLargestSquare(board):
    answer = 0
    number_board = [[0 if e == 'X' else 1 for e in row] for row in board]
    for i in range(1, len(number_board)):
        for j in range(1, len(number_board[0])):
            if number_board[i][j] == 1:
                number_board[i][j] = min(number_board[i - 1][j], number_board[i - 1][j - 1], number_board[i][j - 1]) + 1
                answer = max(answer, number_board[i][j])
    return answer ** 2


# 아래 코드는 출력을 위한 테스트 코드입니다.
testBoard = [['X', 'O', 'O', 'O', 'X'],
             ['X', 'O', 'O', 'O', 'O'],
             ['X', 'X', 'O', 'O', 'O'],
             ['X', 'X', 'O', 'O', 'O'],
             ['X', 'X', 'X', 'X', 'X']]

print(findLargestSquare(testBoard))
