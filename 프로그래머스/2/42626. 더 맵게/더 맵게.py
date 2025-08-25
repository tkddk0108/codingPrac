import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
        
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        new = a+b*2
        heapq.heappush(scoville, new)
        answer += 1
    return answer





# def check(scoville, K):
#     for i in scoville:
#         if i < K:
#             return False
#     return True

# # 루프문에서 heap.peek이 K 이상일 때, answer를 더하지 않고 즉시 0을 리턴하는가
# # heap의 size가 2보다 작아 루프에서 탈출했을 때, heap.peek이 K 이상인지 확인 후 answer를 return 하는가
# # 이 두 가지만 확인하면 쉽게 통과하실 수 있습니다.
# def solution(scoville, K):
#     answer = 0
#     scoville = sorted(scoville)
#     while check(scoville, K) == False:
#         if len(scoville) >= 2:
#             new = scoville[0] + scoville[1]*2
#             scoville = scoville[2:]
#             scoville.append(new)
#             scoville = sorted(scoville)
#             answer += 1
#         else:
#             return -1
        
#     return answer