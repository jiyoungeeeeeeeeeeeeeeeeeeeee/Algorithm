def solution(n):
    lst = [i for i in range(1, n + 1)]

    left = 0
    right = 0
    total = 0
    cnt = 0

    while right <= len(lst):
        if total < n:
            if right == len(lst):
                break

            total += lst[right]
            right += 1

        elif total > n:
            total -= lst[left]
            left += 1

        else:
            cnt += 1
            total -= lst[left]
            left += 1

    return cnt