def solution(s):
    answer = []
    result = s
    time, rm  = 0, 0
    while result != "1":
        rm += result.count ("0")
        result = str(bin(len(result) - result.count ("0"))[2:])
        time += 1
    return [time, rm]