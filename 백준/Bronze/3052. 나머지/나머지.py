nums = {int(input()) for _ in range(10)}
quotient = set()

for i in nums:
    quotient.add(i%42)
print(len(quotient))