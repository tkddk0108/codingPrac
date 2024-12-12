a, b = map(int, input().strip().split(' '))
answer = ''
for i in range(b):
    answer += '*'*a + '\n'
print(answer)