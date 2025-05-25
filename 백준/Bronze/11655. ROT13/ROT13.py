from collections import deque
S = input()
upper = deque([chr(c) for c in range(ord('A'),ord('Z')+1)])
lower = deque([chr(c) for c in range(ord('a'),ord('z')+1)])

upper.rotate(-13)
lower.rotate(-13)

result = ''

for s in S:
    if s.isupper(): # 문자열일 경우
        idx = (ord(s) - ord('A'))
        result += upper[idx]
    elif s.islower():
        idx = (ord(s) - ord('a'))
        result += lower[idx]
    else:
        result += s

print(result)
        