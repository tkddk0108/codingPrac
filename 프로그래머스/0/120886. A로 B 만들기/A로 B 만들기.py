def solution(before, after):
    after = list(after)
    for i in before:
        if i in after:
            after.remove(i)
    if after == []:
        return 1
    else:
        return 0
