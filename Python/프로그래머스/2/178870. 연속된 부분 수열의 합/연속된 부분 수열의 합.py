def solution(sequence, k):
    answer = []
    idx = 0
    idx2 = 0
    total = 0

    while idx < len(sequence):

        while idx2 < len(sequence) and total < k:
            total += sequence[idx2]
            idx2 += 1

        if total == k:
            answer.append([idx, idx2 - 1])

        total -= sequence[idx]
        idx += 1

    answer.sort(key=lambda x: (x[1] - x[0], x[0]))

    return answer[0]