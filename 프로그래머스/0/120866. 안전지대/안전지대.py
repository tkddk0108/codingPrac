def bomb(board,a,b):
    n = len(board)
    for i in range(max(0,a-1), min(a+2, n)):
        for j in range(max(0, b-1), min(b+2, n)):
            board[i][j] = 1 
    return board

def solution(board):
    cnt = 0
    board1 = [[0] * len(board) for _ in range(len(board))]
              
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                board1 = bomb(board1, i, j)
    for a in board1: print(a)
    
    for i in range(len(board)):
        for j in range(len(board)):
            if board1[i][j] == 0: cnt += 1
    
    return cnt