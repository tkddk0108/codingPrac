def solution(keymap, targets):
    answer = []

    for word in targets:
        total = 0
        for i in word:
            value = []
            for k in range(len(keymap)):
                if i in keymap[k]:
                    #print(i, key, keymap)
                    value.append(keymap[k].index(i))
                else: value.append(101)
            #print(i, keymap[value.index(min(value))], value)
            
            min_index = value.index(min(value))
            
            if value and min(value) != 101 and i in keymap[min_index]:
                #print(keymap[value.index(min(value))].index(i))
                #if 101 not in keymap[value.index(min(value))]:
                total += keymap[min_index].index(i)+1
            #else:
                #total += -1
            #print(value, total)
            if not value or min(value) == 101:
                total = -1
                break
            #print(value, total)
            value = []
        answer.append(total)
        #print(answer)
        total = 0
    return answer