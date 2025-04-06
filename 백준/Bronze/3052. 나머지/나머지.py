nums = [int(input()) for _ in range(10)]
quotient = []

for i in nums:
    qutt = i%42

    if qutt not in quotient:
        quotient.append(qutt)  
        
print(len(quotient))


  
