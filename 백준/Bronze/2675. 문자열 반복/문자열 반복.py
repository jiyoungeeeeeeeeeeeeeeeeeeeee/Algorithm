T = int(input())

for _ in range(T):
    R,P = input().split()
    R = int(R)
    
    for char in P:
        print(char*R , end = '')
    print()
        