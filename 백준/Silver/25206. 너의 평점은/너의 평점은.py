total = 0
sum_rate = 0

for i in range(20):
    sub,rate,grade = input().split()
    # print(sub,rate,grade)
    
    rate = float(rate)

    if grade == 'A+':
        total += rate*4.5
        sum_rate += rate

    if grade == 'A0':
        total += rate*4.0
        sum_rate += rate

    if grade == 'B+':
        total += rate*3.5
        sum_rate += rate

    if grade == 'B0':
        total += rate*3.0
        sum_rate += rate

    if grade == 'C+':
        total += rate*2.5
        sum_rate += rate

    if grade == 'C0':
        total += rate*2.0
        sum_rate += rate

    if grade == 'D+':
        total += rate*1.5
        sum_rate += rate

    if grade == 'D0':
        total += rate*1.0
        sum_rate += rate

    if grade == 'F':
        total += rate*0
        sum_rate += rate

    if grade == 'P':
        continue

print(total/sum_rate)

        
        