a= int(input())
b= int(input())
c= int(input())

multiply = a*b*c
digits = [int(d) for d in str(multiply)]


cnt_0 = 0
cnt_1 = 0
cnt_2 = 0
cnt_3 = 0
cnt_4 = 0
cnt_5 = 0
cnt_6 = 0
cnt_7 = 0
cnt_8 = 0
cnt_9 = 0

for m in digits:
    if m == 0:
        cnt_0 += 1
    elif m == 1:
        cnt_1 += 1
    elif m == 2:
        cnt_2 += 1
    elif m == 3:
        cnt_3 += 1
    elif m == 4:
        cnt_4 += 1
    elif m == 5:
        cnt_5 += 1
    elif m == 6:
        cnt_6 += 1
    elif m == 7:
        cnt_7 += 1
    elif m == 8:
        cnt_8 += 1
    elif m == 9:
        cnt_9 += 1

print(cnt_0,
cnt_1, 
cnt_2,
cnt_3,
cnt_4,
cnt_5,
cnt_6,
cnt_7,
cnt_8,
cnt_9 , sep = '\n')