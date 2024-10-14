def solution(numbers):
    answer = 0
    max1 = max(numbers)
    remove = numbers.remove(max(numbers))
    max2 = max(numbers)
    return max1 * max2