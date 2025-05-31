m,n = map(int,input().split())

# 소수는 1과 자기 自身만 약수로 갖는 것

for i in range(m , n+1):
    if i < 2:
        continue
    for j in range(2, int(i**0.5)+1):
        if i% j == 0:
            break
    else:
        print(i)         
