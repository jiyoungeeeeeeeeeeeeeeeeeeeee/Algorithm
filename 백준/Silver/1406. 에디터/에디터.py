import sys
text = sys.stdin.readline().strip()
m = int(sys.stdin.readline().strip())

cursor_right = [] # 역순으로 저
cursor_left = []

cursor_left.extend(text)

for _ in range(m):
    edit = input().split()
    if edit[0] == 'L':
        if cursor_left:
            cursor_right.append(cursor_left.pop())
    elif edit[0] == 'D':
        if cursor_right:
            cursor_left.append(cursor_right.pop())
    elif edit[0] == 'B':
        if cursor_left:
            cursor_left.pop()
    elif edit[0] == 'P':
        cursor_left.append(edit[1])

print(''.join(cursor_left + list(reversed(cursor_right))))



