n,b = input().split()
b = int(b)
total = 0

n = n[::-1]

for i in range(len(n)):
    if n[i].isdigit():
        value = int(n[i])
    else:
        value = ord(n[i].upper())-ord('A') + 10
    
    value = value * (b**i)
    # print(value)
    total += value

print(total)