def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]

    for word in babbling:
        i = 0
        prev = ""

        while i < len(word):
            matched = False

            for w in words:
                if word[i:i + len(w)] == w and prev != w:
                    i += len(w)
                    prev = w
                    matched = True
                    break

            if not matched:
                break

        if i == len(word):
            answer += 1

    return answer