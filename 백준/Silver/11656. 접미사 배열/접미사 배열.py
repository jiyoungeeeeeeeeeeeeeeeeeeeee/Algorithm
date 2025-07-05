S = input()
suffix = []
for i in range(len(S)):
    word = S[i:]
    suffix.append(word)

suffix.sort()


for i in range(len(S)):
    print(suffix[i])
