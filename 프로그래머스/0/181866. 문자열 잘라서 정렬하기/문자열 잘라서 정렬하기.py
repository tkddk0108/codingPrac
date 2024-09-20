def solution(myString):
    answer = myString.split("x")
    arr = []
    for i in answer:
       if i != "": arr.append(i)
    arr.sort()
    return arr