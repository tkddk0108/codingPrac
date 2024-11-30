def solution(keymap, targets):
    answer = []

    for word in targets:
        total = 0
        for i in word:
            value = []
            for k in range(len(keymap)):
                if i in keymap[k]:
                    value.append(keymap[k].index(i))
                else: value.append(101)
            
            min_index = value.index(min(value))
            
            if value and min(value) != 101 and i in keymap[min_index]:
                total += keymap[min_index].index(i)+1
            if not value or min(value) == 101:
                total = -1
                break
        answer.append(total)
        total = 0
    return answer