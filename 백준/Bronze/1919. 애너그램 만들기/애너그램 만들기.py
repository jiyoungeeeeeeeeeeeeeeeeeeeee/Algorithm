import sys

word1 = sys.stdin.readline().strip()
word2 = sys.stdin.readline().strip()

cnt1 = [0]*26
cnt2 = [0]*26

for w1 in word1:
    idx = ord(w1) - ord('a')
    cnt1[idx] += 1

for w2 in word2:
    idx = ord(w2) - ord('a')
    cnt2[idx] += 1

answer = 0

for i in range(26):
    answer += abs(cnt1[i] - cnt2[i])

print(answer)