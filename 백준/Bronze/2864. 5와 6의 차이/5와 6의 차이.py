import sys

A,B = list(sys.stdin.readline().split())

def trans5(t):
    lst5 = []

    for b in t:
        if b == '5':
            lst5.append('6')
        else:
            lst5.append(b)
        
    return lst5

def trans6(t):
    lst6 = []

    for b in t:
        if b == '6':
            lst6.append('5')
        else:
            lst6.append(b)
        
    return lst6

at5 = int(''.join(trans5(A)))
at6 = int(''.join(trans6(A)))
bt5 = int(''.join(trans5(B)))
bt6 = int(''.join(trans6(B))) 

s5 = at5 + bt5
s6 = at6 + bt6 
print(min(s5 , s6), max(s5,s6))


        
    