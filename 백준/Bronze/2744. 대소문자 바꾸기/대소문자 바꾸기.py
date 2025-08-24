text = input()

for t in text:
    if t.islower():
        print(t.upper() , end = '')
    else:
        print(t.lower() , end = '')