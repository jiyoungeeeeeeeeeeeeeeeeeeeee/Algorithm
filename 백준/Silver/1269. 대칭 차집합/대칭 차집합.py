import sys
a_cnt , b_cnt = map(int,sys.stdin.readline().split())

a = set(map(int,sys.stdin.readline().split()))
b = set(map(int,sys.stdin.readline().split()))

diff1 = a-b
diff2 = b-a

print(len(diff1) + len(diff2))
