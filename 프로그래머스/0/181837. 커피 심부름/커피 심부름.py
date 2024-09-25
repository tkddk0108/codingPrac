def solution(order):
    answer = 0
    four = ["iceamericano", "americanoice","hotamericano", "americanohot", "americano", "anything"]
    five = ["icecafelatte", "cafelatteice","hotcafelatte", "cafelattehot", "cafelatte"]
    for i in order:
        if i in four: answer += 4500
        else: answer += 5000 
    return answer