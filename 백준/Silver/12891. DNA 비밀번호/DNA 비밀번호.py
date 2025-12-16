import sys

s,p = map(int,sys.stdin.readline().split())
dna = sys.stdin.readline().strip()
a,c,g,t = map(int,sys.stdin.readline().split())

cnt_a,cnt_c,cnt_g,cnt_t = 0,0,0,0
ans = 0

for i in range(p):
    if dna[i] == 'A':
        cnt_a +=1
    elif dna[i] == 'C':
        cnt_c +=1
    elif dna[i] == 'G':
        cnt_g += 1
    elif dna[i] == 'T':
        cnt_t += 1
    
if cnt_a >= a and cnt_c >=c and cnt_g >= g and cnt_t >= t:
    ans += 1

for j in range(s-p):
    if dna[j] == 'A':
        cnt_a -= 1
    elif dna[j] == 'C':
        cnt_c -= 1
    elif dna[j] == 'G':
        cnt_g -= 1
    elif dna[j] == 'T':
        cnt_t -= 1
    
    if dna[j+p] == 'A':
        cnt_a += 1
    elif dna[j+p] == 'C':
        cnt_c += 1
    elif dna[j+p] == 'G':
        cnt_g += 1
    elif dna[j+p] =='T':
        cnt_t += 1

    if cnt_a >= a and cnt_c >=c and cnt_g >= g and cnt_t >= t:
        ans += 1

print(ans)
    