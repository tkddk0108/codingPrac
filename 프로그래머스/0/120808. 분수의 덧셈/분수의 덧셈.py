def solution(numer1, denom1, numer2, denom2):
    answer = []
    if numer1 != numer2:
        down = denom1 * denom2
        up = denom1*numer2 + denom2*numer1
        li = []
    else: 
        down = denom1
        up = numer1 + numer2
    last = 1
    for i in range(2, 1000):
        if up % i == 0 and down % i == 0:
            last = i

    answer.append(up // last)
    answer.append(down // last)
    return answer