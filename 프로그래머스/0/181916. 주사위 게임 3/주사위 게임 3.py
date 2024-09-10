from collections import Counter

def solution(a, b, c, d):
    answer = 0
    num = [a, b, c, d]
    counter = Counter(num)
    
    one = [num for num, count in counter.items() if count == 1]
    two = [num for num, count in counter.items() if count == 2]
    three = [num for num, count in counter.items() if count == 3]
    
    # 모든 값이 같은 경우
    if a == b == c == d:
        answer = 1111 * a
    # 세 개의 값이 같고, 나머지 하나가 다른 경우
    elif len(three) == 1 and len(one) == 1:
        answer = (10 * three[0] + one[0]) * (10 * three[0] + one[0])
    # 두 쌍씩 값이 같은 경우
    elif len(two) == 2:
        answer = (two[0] + two[1]) * abs(two[0] - two[1])
    # 한 쌍만 값이 같고 나머지 두 개가 다른 경우
    elif len(two) == 1 and len(one) == 2:
        answer = one[0] * one[1]
    # 나머지 경우는 가장 작은 값 반환
    else:
        answer = min(num)
    
    return answer