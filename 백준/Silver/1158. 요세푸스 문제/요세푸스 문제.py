from collections import deque

n,k = map(int,input().split())
people = [ i for i in range(1,n+1)]
arrange = []
dq = ()
dq = deque(people)
   

while dq:
    dq.rotate(-k)    
    arrange.append(dq.pop())
    
print("<"+ ", ".join(map(str,arrange))+">")
