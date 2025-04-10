s = input()
i = 0
cnt = 0

while i < len(s):
    if s[i:i+3] == 'dz=':
        cnt += 1
        i += 3
    elif s[i:i+2] in ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']:
        cnt += 1
        i += 2
    else:
        cnt += 1
        i += 1

print(cnt)