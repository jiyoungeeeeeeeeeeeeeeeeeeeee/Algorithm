submit = [int(input()) for _ in range(28)]
std = list(range(1,31))

for s in submit:
    std.remove(s)

for s in sorted(std):
    print(s)