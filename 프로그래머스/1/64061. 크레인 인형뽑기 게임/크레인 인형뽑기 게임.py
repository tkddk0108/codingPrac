def solution(board, moves):
    '''
    moves: [1,5,3,5,1,2,1,4]
    [0,0,0,0,0] -> val
    [0,0,1,0,3]
    [0,2,5,0,1]
    [4,2,4,4,2]
    [3,5,1,3,1]
    1 고양이 /2 단무지/ 3-오리/ 4-어피치/ 5-프로도
    어피치 오리 고양이 고양이 오리 단무지 없음 어피치
    4 3 1 1 3 2 4
    '''
    stack = []
    cnt = 0
    for i in range(len(moves)):
        for val in board:
            if val[moves[i]-1] == 0: continue
            else: 
                stack.append(val[moves[i]-1])
                val[moves[i]-1] = 0
                
                if len(stack) >= 2 and stack[-1] == stack[-2]:
                    stack.pop()
                    stack.pop()
                    cnt += 2
                break
    print(stack)
    return cnt
