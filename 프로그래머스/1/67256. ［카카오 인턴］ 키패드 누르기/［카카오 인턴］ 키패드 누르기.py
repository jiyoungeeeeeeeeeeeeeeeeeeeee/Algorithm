def solution(numbers, hand):
    answer = ''

    pos = {
        1: (0, 0), 2: (1, 0), 3: (2, 0),
        4: (0, 1), 5: (1, 1), 6: (2, 1),
        7: (0, 2), 8: (1, 2), 9: (2, 2),
        0: (1, 3)
    }

    left_pos = (0, 3)
    right_pos = (2, 3)

    if hand == "right":
        main_hand = 'R'
    else:
        main_hand = 'L'

    for n in numbers:
        target = pos[n]

        if n in [1, 4, 7]:
            answer += 'L'
            left_pos = target

        elif n in [3, 6, 9]:
            answer += 'R'
            right_pos = target

        else:
            left_distance = abs(left_pos[0] - target[0]) + abs(left_pos[1] - target[1])
            right_distance = abs(right_pos[0] - target[0]) + abs(right_pos[1] - target[1])

            if left_distance < right_distance:
                answer += 'L'
                left_pos = target

            elif left_distance > right_distance:
                answer += 'R'
                right_pos = target

            else:
                answer += main_hand

                if main_hand == 'L':
                    left_pos = target
                else:
                    right_pos = target

    return answer