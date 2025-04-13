n,b = map(int,input().split())
result = ''


while n > 0:
    remainder = n%b
    if remainder >= 10:
        result = chr(ord('A') + remainder - 10) + result
    
    else :
        result = str(remainder) + result
    n = n // b
print(result.upper())