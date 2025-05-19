import sys
from collections import Counter

n = int(sys.stdin.readline())
arr = (sys.stdin.readline().split())

result = [-1]*n # 결과값 초기 세팅
f = Counter(arr) # 빈도수 dict 형태로 저장
stack = [] # 현재값 임시저장 | 오큰수를 찾기 위한 저장소

for i in range(n):
    while stack and f[arr[stack[-1]]] < f[arr[i]]: # stack에 저장된 현재 수 보다 현재수가 더 클때 
        result[stack.pop()] = arr[i]
    stack.append(i)

print(*result)



    