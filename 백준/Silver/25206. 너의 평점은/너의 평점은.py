grade_dict = {
    'A+': 4.5, 'A0': 4.0,
    'B+': 3.5, 'B0': 3.0,
    'C+': 2.5, 'C0': 2.0,
    'D+': 1.5, 'D0': 1.0,
    'F': 0.0
}

total = 0
total_rate = 0

for _ in range(20):
    subject,rate,grade = input().split()
    rate = float(rate)

    if grade == 'P':
        continue
    
    total += rate*grade_dict[grade]
    total_rate += rate

print(total/total_rate)