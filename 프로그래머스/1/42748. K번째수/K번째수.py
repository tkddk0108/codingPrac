def solution(array, commands):
    answer = []
    for com in commands:
        i, j, k = com[0], com[1], com[2]
        box = sorted(array[i-1:j])
        print(box)
        if len(box) >= k-1:
            answer.append(box[k-1])
    return answer