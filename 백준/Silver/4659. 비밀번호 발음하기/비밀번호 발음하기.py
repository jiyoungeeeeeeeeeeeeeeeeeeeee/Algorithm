import sys

first = ['a','e','i','o','u']

while True:
    word = sys.stdin.readline().strip()
    if word == 'end':
        break
    acceptable = True
    
    if 'a' in word or 'e' in word or 'i' in word or 'o' in word or 'u' in word:
        acceptable = True
    else:
        acceptable = False
        
    if acceptable:
        for i in range(len(word)-2):
            if word[i] in first and word[i+1] in first and word[i+2] in first:
                acceptable = False
                break
    
            elif word[i] not in first and word[i+1] not in first and word[i+2] not in first:
                acceptable = False
                break

    if acceptable:
        for i in range(len(word)-1):
            if word[i] == word[i+1]:
                if word[i] != 'e' and word[i] != 'o':
                    acceptable = False
                    break              
    
    if acceptable:
        print(f"<{word}> is acceptable.")
    else:
        print(f"<{word}> is not acceptable.")

                