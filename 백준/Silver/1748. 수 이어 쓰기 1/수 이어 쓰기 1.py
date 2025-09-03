import sys
n = int(sys.stdin.readline())

ans = 0
start = 1
digits = 1


while start * 10 <= n:
    ans += (start * 10 - start) * digits
    start *= 10
    digits += 1

ans += (n - start + 1 ) *digits 
print(ans)