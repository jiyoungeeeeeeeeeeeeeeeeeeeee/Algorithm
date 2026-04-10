while 1:
    s = input()

    if s == '#':
        break

    if s.count('1') % 2 == 0:
        print(s[:-1] + '0' if s[-1] == 'e' else s[:-1] + '1')
    else:
        print(s[:-1] + '1' if s[-1] == 'e' else s[:-1] + '0')