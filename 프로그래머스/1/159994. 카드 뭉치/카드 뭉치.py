def solution(cards1, cards2, goal):
    answer = ''
    for i in goal:
        if i in cards1:
            if i != cards1[0]: return "No"
            else: cards1.remove(i)
        if i in cards2:
            if i != cards2[0]: return "No"
            else: cards2.remove(i)
    return "Yes"