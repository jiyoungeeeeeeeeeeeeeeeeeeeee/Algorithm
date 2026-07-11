from collections import Counter

def solution(str1, str2):
    
    def make_list(s):

        s = s.lower()
        result = []

        for i in range(len(s) - 1):
            word = s[i:i+2]

            if word.isalpha():
                result.append(word)

        return Counter(result)
    
    union  = make_list(str1) | make_list(str2)
    inter  = make_list(str1) & make_list(str2)
    
    a = sum(inter.values())
    b = sum(union.values())
    if sum(union.values()) == 0:
        return 65536
    return int(a/b*65536)
    
    # return 