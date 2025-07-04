S = input()

for s in S:
    if s.isupper():
        rot = chr((ord(s) - ord('A') + 13) % 26 + ord("A"))
        print(rot ,end = '')

    elif s.islower():
        rot = chr((ord(s) - ord('a') + 13) % 26 + ord("a"))
        print(rot ,end = '')
    else:
        print(s , end = '')