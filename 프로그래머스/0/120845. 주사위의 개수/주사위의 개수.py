def solution(box, n):
    width, length, height = 0, 0, 0
    for i in range(1, 100):
        if n*i <= box[0]: width += 1
    for i in range(1, 100):
        if n*i <= box[1]: length += 1
    for i in range(1, 100):
        if n*i <= box[2]: height += 1
    print(width, length, height)
    return width*length*height