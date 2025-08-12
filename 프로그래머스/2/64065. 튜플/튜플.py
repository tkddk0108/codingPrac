def solution(s):
    new = {}
    num = ""
    for i in s:
        if i.isdigit():
            num += i

        elif i in "}," and num != "":
            if num in new:
                new[num] += 1
            else:
                new[num] = 1
            num = ""

    answer = [int(k) for k, v in sorted(new.items(), key=lambda x:x[1], reverse=True)]
    return answer