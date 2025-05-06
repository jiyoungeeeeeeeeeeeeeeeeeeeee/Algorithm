n = int(input())
six = []

for i in range(2666800):
    if '666' in str(i): 
        six.append(i)

print(six[n - 1]) 
