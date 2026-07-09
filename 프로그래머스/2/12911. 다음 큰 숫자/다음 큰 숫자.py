def solution(n):
    answer = 0
    n2 = bin(n)[2:]
    ncnt = str(n2).count('1')
    
    for i in range(n+1,1000000):
        trans = bin(i)[2:]
        cnt = str(trans).count('1')
        
        if cnt == ncnt:
            return i 