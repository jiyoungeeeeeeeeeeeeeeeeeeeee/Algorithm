try:
    while True:
        a,b = map(int,input().split())
        if a > 0 and b < 10:
            print(a+b)
        else: break
except EOFError:
    pass