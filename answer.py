
from collections import defaultdict


keypad = list(map(int, list(input())))

key = [keypad[i:i+3]for i in range(3)]

code = list(map(int, list(input())))

d = defaultdict(list)

i = 0
j = 0
for n in keypad:
    d[n] = [i, j%3]
    j+=1
    if j % 3 == 0:
        i+=1

ans = 0

for i in range(1,len(code)):
    if code[i] == code[i-1]:
        ans+=0
    elif abs(d[code[i]][0] - d[code[i-1]][0]) > 1 or  abs(d[code[i]][1] - d[code[i-1]][1]) >  1:
        ans+=2
    else:
        ans+=1

print(ans)