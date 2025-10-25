from collections import deque
import sys

T = int(sys.stdin.readline())

def reverse_drop(AC : str , arr_lst : deque):
    rev = False 

    for a in AC:
        if a == 'R':
            rev = not rev

        if a == 'D':
            if not arr_lst:
                print('error')
                return None
                
            if rev:
                arr_lst.pop()
            else:
                arr_lst.popleft()

    if rev:
        arr_lst.reverse()

    return arr_lst


for t in range(T):
    ac = input()
    arr_len = int(input())
    arr = deque(map(int, filter(None, input().strip('[').strip(']').split(','))))

    res = reverse_drop(ac, arr)
    if res is not None:
        print('[' + ','.join(map(str, res)) + ']')
