n,b = input().split()
b = int(b)
total = 0


for i in range(len(n)):
    if n[i].isdigit():
        value = int(n[i])
    else:
        value = ord(n[i].upper())-ord('A') + 10
    
    total += value*(b**(len(n) -1 - i))

print(total)