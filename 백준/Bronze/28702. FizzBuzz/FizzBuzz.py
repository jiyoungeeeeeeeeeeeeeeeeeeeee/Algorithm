import sys
result = []
pos = []

for i in range(3):
    text = sys.stdin.readline().strip()

    if text.isnumeric():
        result.append(int(text))
        pos.append(i)

    else:
        result.append(text)

if pos:
    h = result[pos[-1]] + (3 - pos[-1])

    if   h % 3 == 0 and h % 5 == 0:
        print('FizzBuzz')
    elif h % 3 == 0 and h % 5 != 0:
        print('Fizz')
    elif h % 3 != 0 and h % 5 == 0:
        print('Buzz')
    else:
        print(h)