n = int(input())
cnt = 0

for i in range(n):
  word = input()
  is_group = True 

  for j in range(len(word)-1):
    if word[j] != word[j+1]:
      if word[j] in word[j+1:]:
        is_group = False
  
  if is_group:
    cnt += 1

print(cnt)
