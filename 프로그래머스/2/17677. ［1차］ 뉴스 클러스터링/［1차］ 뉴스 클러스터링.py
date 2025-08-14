def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    word1, word2 = [], []
    
    # 2글자씩 잘라서 알파벳만 추가
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            word1.append(str1[i] + str1[i+1])
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            word2.append(str2[i] + str2[i+1])
    
    # 모든 원소의 중복 제거된 집합 만들기
    all_words = set(word1) | set(word2)
    
    inter_count = 0
    union_count = 0
    
    for w in all_words:
        count1 = word1.count(w)
        count2 = word2.count(w)
        inter_count += min(count1, count2)  
        union_count += max(count1, count2)  
    
    if union_count == 0:
        return 65536
    
    return int(inter_count / union_count * 65536)