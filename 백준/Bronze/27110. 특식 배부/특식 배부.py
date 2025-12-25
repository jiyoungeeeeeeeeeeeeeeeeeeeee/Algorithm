import sys

n = int(sys.stdin.readline())
fri,soy,yang = map(int,sys.stdin.readline().split())

def updown (A):
    if A >= n:
        return n
    else:
        return A
    
print(updown(fri)+updown(soy)+updown(yang))