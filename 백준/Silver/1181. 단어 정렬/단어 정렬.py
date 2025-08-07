n = int(input())

text_set = set()
for i in range(n):
    text = input()

    text_set.add(text)


sorted_words = sorted(text_set, key=lambda x: (len(x), x))

for s in sorted_words:
    print(s)
