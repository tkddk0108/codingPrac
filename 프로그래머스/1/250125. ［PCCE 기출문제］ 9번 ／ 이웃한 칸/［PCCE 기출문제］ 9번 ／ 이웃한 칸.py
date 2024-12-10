def solution(board, h, w):
    answer = 0
    point = board[h][w]
    # up
    if h != 0 and board[h-1][w] == point: answer += 1
    # down
    if h != len(board)-1 and board[h+1][w] == point: answer += 1
    #right
    if w != len(board[h])-1 and board[h][w+1] == point: answer += 1
    #left
    if w != 0 and board[h][w-1] == point: answer += 1
    
    return answer