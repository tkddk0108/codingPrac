'''
<area>
single: 1제곱 | double: 2제곱 | triple: 3제곱
<option>
* -> (i-1) * 2  & i * 2 
    첫번째에 나오면 첫번째 껏만 i*2 
# -> -i
'''
def solution(dartResult):
    li = []
    dartResult = list(map(str, dartResult))
    for i in range(len(dartResult)):
        # 숫자처리
        if dartResult[i].isdigit():
        # 8번째 줄 if score[-1] == 0 and score[-2] == 1: 에서
        # 첫 번째 다트 점수가 10점이 아닌 0점일 때는 score[-2] 가 없기 때문에 그런거 같네요
            if dartResult[i] == '0' and len(li) >= 1 and li[-1] == 1:
                li.pop() 
                li.append(10)
            else:
                li.append(int(dartResult[i]))
            continue
        # 제곱처리
        elif dartResult[i] == "D":
            li[-1] = int(li[-1])**2
        elif dartResult[i] == "T":
            li[-1] = int(li[-1])**3
        # * # 처리
        elif dartResult[i] == "*":
            li[-1] = li[-1]*2
            if len(li) > 1: li[-2] = li[-2]*2
        elif dartResult[i] == "#":
            li[-1] = -li[-1]
        #print(li)
    return sum(li)
        