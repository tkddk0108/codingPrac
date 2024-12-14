def solution(players, callings):
    # 딕셔너리 생성: 선수 이름 -> 현재 순위
    rank = {player: idx for idx, player in enumerate(players)}
    #print(rank)
    # 순위 조정
    for player in callings:
        current_rank = rank[player]
        #print(current_rank)
        # 현재 순위 앞의 선수와 교체
        front_player = players[current_rank - 1]
        # 순위 업데이트
        #print(front_player)
        players[current_rank - 1], players[current_rank] = players[current_rank], players[current_rank - 1]
        rank[player] -= 1
        rank[front_player] += 1
    return players