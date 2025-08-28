# [10, 8, 5, 4, 3] 의 인용횟수를 가진 교수가 있다면
# 10번 이상 인용 횟수를 가진 논문은 1편입니다. 이때 H-Index는 1입니다.
# 8번 이상 인용 횟수를 가진 논문은 2편입니다. 이때 H-Index는 2입니다.
# 5번 이상 인용 횟수를 가진 논문은 3편입니다. 이때 H-Index는 3입니다.
# 4번 이상 인용 횟수를 가진 논문은 4편입니다. 이때 H-Index는 4입니다.
# 3번 이상 인용 횟수를 가진 논문은 5편입니다. 이때 H-Index는 3입니다.
def solution(citations):
    answer = []
    for i in citations:
        answer.append(min(i,sum([1 for x in citations if x >= i])))
    return max(answer)