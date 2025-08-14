dwarf = list(int(input()) for _ in range(9))

total = sum(dwarf)
fake_dwarf = total - 100

for i in range(9):
    for j in range(i):
        if dwarf[i] + dwarf[j] == fake_dwarf:
            fake1 = dwarf[i]
            fake2 = dwarf[j]
            dwarf.remove(fake1)
            dwarf.remove(fake2)
            break
    else:
        continue
    break
    
dwarf.sort()
for f in dwarf:
    print(f)
