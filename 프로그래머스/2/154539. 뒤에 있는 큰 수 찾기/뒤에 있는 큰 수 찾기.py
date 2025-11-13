def solution(numbers):
    n = len(numbers)
    answer = [-1] * n
    stack = []  # "가능성 있는 후보"를 저장

    for i in range(n - 1, -1, -1):   # 오른쪽 → 왼쪽
        while stack and stack[-1] <= numbers[i]:
            stack.pop()
        if stack:
            answer[i] = stack[-1]
        stack.append(numbers[i])

    return answer