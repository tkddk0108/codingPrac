import heapq

def solution(operations):
    heap = []
    for val in operations:
        oper, num = val.split(" ")
        num = int(num)
        if oper == "D":
            if not heap:
                continue
            if num == 1:
                heap.remove(max(heap))
                heapq.heapify(heap)
            elif num == -1:
                heapq.heappop(heap)
        elif oper == "I":
            heapq.heappush(heap, num)
    
    if not heap:
        return [0,0]
    else:
        return [max(heap), min(heap)]