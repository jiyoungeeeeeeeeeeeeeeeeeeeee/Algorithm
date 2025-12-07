import sys

n = int(sys.stdin.readline())

for i in range(n):
    text1, text2 = sys.stdin.readline().rstrip().split()
    
    if sorted(text1) == sorted(text2):
        print(f"{text1} & {text2} are anagrams.")
    else:
        print(f"{text1} & {text2} are NOT anagrams.")
