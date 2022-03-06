# https://programmers.co.kr/learn/courses/30/lessons/60062?language=python3
from itertools import permutations


def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)

    answer = len(dist) + 1  # 점검 불가능한 경우를 위해 최대값 + 1
    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            count = 1
            end = weak[start] + friends[count - 1]
            for position in range(start, start + length):
                if end < weak[position]:
                    count += 1
                    if count > len(dist):
                        break
                    end = weak[position] + friends[count - 1]
            answer = min(answer, count)

    return -1 if answer > len(dist) else answer


if __name__ == '__main__':
    if solution(12, [1, 5, 6, 10], [1, 2, 3, 4]) == 2:
        print(f'TESTCASE 1 PASSED!')
    if solution(12, [1, 3, 4, 9, 10], [3, 5, 7]) == 1:
        print(f'TESTCASE 2 PASSED!')
