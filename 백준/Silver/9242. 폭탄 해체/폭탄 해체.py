import sys

def solve():
    digit_map = {
        ''.join(['***', '* *', '* *', '* *', '***']): '0',
        ''.join(['  *', '  *', '  *', '  *', '  *']): '1',
        ''.join(['***', '  *', '***', '*  ', '***']): '2',
        ''.join(['***', '  *', '***', '  *', '***']): '3',
        ''.join(['* *', '* *', '***', '  *', '  *']): '4',
        ''.join(['***', '*  ', '***', '  *', '***']): '5',
        ''.join(['***', '*  ', '***', '* *', '***']): '6',
        ''.join(['***', '  *', '  *', '  *', '  *']): '7',
        ''.join(['***', '* *', '***', '* *', '***']): '8',
        ''.join(['***', '* *', '***', '  *', '***']): '9'
    }

    lines = []
    for _ in range(5):
        lines.append(sys.stdin.readline().rstrip('\n'))

    result = ''
    idx = 0

    while idx < len(lines[0]):
        shape = ''

        for i in range(5):
            shape += lines[i][idx:idx+3]

        if shape not in digit_map:
            print('BOOM!!')
            return

        result += digit_map[shape]
        idx += 4

    if int(result) % 6 == 0:
        print('BEER!!')
    else:
        print('BOOM!!')

solve()