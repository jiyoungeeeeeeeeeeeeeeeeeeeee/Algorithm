import sys
n,k = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
cnt = 0

for i in range(n-1,0,-1):
    max_val = max(arr[:i+1])
    max_idx = arr.index(max_val)

    if arr[max_idx] != arr[i]:
        arr[max_idx],arr[i] = arr[i],arr[max_idx] 
        cnt += 1
        if cnt == k:
            print(arr[max_idx] , arr[i])
            break
    else:
        continue

else:
    print(-1)