import heapq

def solution(operations):
    answer = []

    for V in operations:
        i, num = V.split()
        num = int(num)

        if i == 'I':
            heapq.heappush(answer, num)

        elif i == 'D':
            if not answer:
                continue

            if num == -1:
                heapq.heappop(answer)

            elif num == 1:
                max_value = max(answer)
                answer.remove(max_value)
                heapq.heapify(answer)

    if not answer:
        return [0, 0]

    return [max(answer), answer[0]]