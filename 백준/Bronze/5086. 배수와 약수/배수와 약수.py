while True:
    a,b = map(int,input().split())

    if a*b == 0:
        break


    # 기준은 두 번째 숫자이다.
    # 약수 : a < b // 배수 : a > b

    if a < b :
        if b%a == 0:
            print('factor')

    
    elif a > b:
        if a%b == 0:
            print('multiple')
    
        else : 
            print('neither')
    

