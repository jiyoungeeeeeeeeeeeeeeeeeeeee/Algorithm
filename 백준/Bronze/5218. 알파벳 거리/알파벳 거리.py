import sys

n = int(sys.stdin.readline())

def dist_list(lst1, lst2):
    result = []
    i = 0
    while i < len(lst1):
        d = lst2[i] - lst1[i]
        if d < 0:
            d += 26
        result.append(d)
        i += 1
    return result

for _ in range(n):
    w1, w2 = sys.stdin.readline().split()

    s1 = []
    s2 = []

    i = 0
    while i < len(w1):
        s1.append(ord(w1[i]) - ord('A'))
        s2.append(ord(w2[i]) - ord('A'))
        i += 1

    ans = dist_list(s1, s2)

    sys.stdout.write("Distances: " + " ".join(map(str, ans)) + "\n")
