a,b,v = map(int,input().split())
# print(a,b,v)


last_day = v-a
real = a-b
result = (last_day + real - 1) // real + 1
print(result)
