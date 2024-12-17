def solution(wallpaper):
    answer = []
    box = [list(row) for row in wallpaper]
    x_min, x_max, y_min, y_max = float('inf'), 0, float('inf'), 0
    for y in range(len(box)):
        for x in range(len(box[0])):
            if box[y][x] == "#":
                x_min = min(x_min, x)
                x_max = max(x_max, x)
                y_min = min(y_min, y)
                y_max = max(y_max, y)
    return [y_min, x_min, y_max+ 1, x_max+ 1]
