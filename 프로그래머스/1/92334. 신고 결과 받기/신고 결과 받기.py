def solution(id_list, report, k):
    answer = []
    got_warning, email = {}, {}
    for id in id_list: email[id] = 0
    for id in id_list: got_warning[id] = []
    before = set()
    for i in range(len(report)):
        a,b  = map(str, report[i].split())
        if report[i] not in before: 
            got_warning[b].append(a)
        before.add(report[i])
    
    for name in id_list:
        if len(got_warning[name]) >= k:
            for i in got_warning[name]:
                email[i] += 1
                
    return [email[name] for name in email]