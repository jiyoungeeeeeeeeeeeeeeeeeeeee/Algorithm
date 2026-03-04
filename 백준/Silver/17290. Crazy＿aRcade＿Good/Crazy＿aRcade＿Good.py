import sys

r,c = map(int,sys.stdin.readline().split())

bad_rows = set()
bad_cols = set()
all_set  = set(range(1,11))

for i in range(1,11):
    board = sys.stdin.readline().strip()
    
    for j,ch in enumerate(board , start = 1):
        if ch == 'o':
            bad_rows.add(i)
            bad_cols.add(j)

safe_rows = all_set - bad_rows
safe_cols = all_set - bad_cols

result = []
for sr in safe_rows:
    for sc in safe_cols:
        d = abs(sr-r) + abs(sc-c)
        result.append(d)

print(min(result))