def solution(arr, queries):
    answer = []
    new=[]
    
    for i in range(len(queries)):
        s= queries[i][0]
        e= queries[i][1]
        k= queries[i][2]
      
        for idx in range(s,e+1):
            if arr[idx] > k:
                new.append(arr[idx])
        if new: 
            answer.append(min(new))
            new = []
        else: answer.append(-1)

                
    return answer