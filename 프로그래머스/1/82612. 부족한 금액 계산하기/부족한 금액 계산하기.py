def solution(price, money, count):
    answer = -1
    save = []
    for i in range(1,count+1):
        save.append(price * i)
        total = sum(save)
        
    if total - money >= 0:
        return abs(total - money)
    else:
        return 0