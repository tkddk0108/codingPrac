def solution(numbers):
    answer = []
    a = 0
    result = ''
    num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in range(len(numbers)+1):
        if numbers[a:i] in num:
            answer.append(str(num.index(numbers[a:i])))
            a = i
            print(numbers[a:i])
    for i in answer:
        result += i
    return int(result)