def solution(s):
    answer = []
    z_lst = []
    cnt  = 0
    
    while s != '1':
    
        zero = s.count('0')
        z_lst.append(zero)
        s = s.replace('0','')
        long = len(s)
        exchange = []


        while long > 0:
            exchange.append(long % 2)
            long = long // 2
        exchange = exchange[::-1]
        s  = ''.join(map(str,exchange))
        cnt += 1
            
    return cnt , sum(z_lst)