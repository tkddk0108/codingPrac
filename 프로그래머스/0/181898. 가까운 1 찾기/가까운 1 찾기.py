# def solution(arr, idx):
#     answer = 0
#     for i in range(len(arr)):
#         if i >= idx:
#             if arr[i] == 1:
#                 answer = i
#         else: 
#             answer = -1
#     return answer

def solution(arr, idx):
    for i in range(idx,len(arr)):
        if arr[i] == 1:
            return i
    return -1 