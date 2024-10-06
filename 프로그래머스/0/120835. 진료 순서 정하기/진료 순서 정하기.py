def solution(emergency):
    answer = []
    sort = sorted(emergency, reverse = True)
    rank = [sort.index(x) + 1 for x in emergency]
    print(rank)
    return rank