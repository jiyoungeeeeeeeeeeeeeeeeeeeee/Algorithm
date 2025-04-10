Croatia = input()

list_Croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']

for p in list_Croatia:
    Croatia = Croatia.replace(p, '*')

print(len(Croatia))