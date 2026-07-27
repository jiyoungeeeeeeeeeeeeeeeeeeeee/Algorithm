def solution(word):
    lst = ['A','E','I','O','U']
    dic = {}
    idx = 0

    def dfs(current):
            nonlocal idx
            if len(current) == 5:
                return
            
            for l in lst:
                next_word = current + l
                idx += 1
                dic[next_word] = idx
                dfs(next_word)
    dfs('')
    return dic[word]