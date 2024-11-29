def lev1(id):
    #1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    new_id = ''
    for i in range(len(id)):
        if id[i].isalpha: new_id += id[i].lower()
        else: new_id += id[i]
    return new_id

def lev2(id):
    #2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    new_id = ''
    value = "abcdefghijklmnopqrstuvwxyz1234567890-_."
    for i in range(len(id)):
        if id[i] in value: new_id += id[i]
    return new_id

def lev3(id):
    #3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    new_id = ''
    for i in range(len(id)):
        if i>= 1 and id[i] == "." and id[i-1] == ".":
            continue
        else: new_id += id[i]
    return new_id

def lev4(id):
    #4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다
    new_id = ''
    for i in range(len(id)):
        if (i == 0 or i == len(id)-1) and id[i] ==".": continue
        else: new_id += id[i]
    return new_id

def lev5(id):
    #5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if id == "": return "a"
    else: return id

def lev6(id):
    # 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    # 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    if len(id) >= 16: id = id[:15]
    if id[-1] == ".": id = id[:14]
    return id

def lev7(id):
    # new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    if len(id) <= 2:
        plus = id[-1]
        while len(id) != 3:
            id += plus
    return id


def solution(new_id):
    new_id = lev1(new_id)
    new_id = lev2(new_id)
    new_id = lev3(new_id)
    new_id = lev4(new_id)
    new_id = lev5(new_id)
    new_id = lev6(new_id)
    new_id =lev7(new_id)
    return new_id