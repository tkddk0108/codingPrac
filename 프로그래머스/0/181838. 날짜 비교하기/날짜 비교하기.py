from datetime import date

def solution(date1, date2):
    d1 = date(date1[0], date1[1], date1[2])
    d2 = date(date2[0], date2[1], date2[2])
    if d1 < d2 : return 1
    elif d1 >= d2 : return 0