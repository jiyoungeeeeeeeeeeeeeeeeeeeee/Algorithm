h , m = map(int,input().split())
cook = int(input())

all_minute = h*60 + m
finish = all_minute + cook

hour = finish // 60
minute = finish%60

if hour >= 24:
    hour = hour % 24 

print(hour, minute)

