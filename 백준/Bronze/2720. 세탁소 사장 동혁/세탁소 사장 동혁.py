n = int(input())

coins = {'Q' : 25 , 'D' : 10 , 'N' : 5 , 'P': 1 }

for i in range(n):
    c = int(input())
    result = {}

    for coin,value in coins.items():
        count = c//value
        c %= value
        result[coin] = count
    
    print(result['Q'], result['D'], result['N'], result['P'])