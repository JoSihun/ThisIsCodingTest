from itertools import combinations

def sum_chicken_distance(houses, candidate):
    chicken_distance = 0
    for hrow, hcol in houses:
        min_distance = int(1e9)
        for crow, ccol in candidate:
            min_distance = min(min_distance, abs(hrow - crow) + abs(hcol - ccol))
        chicken_distance += min_distance
    return chicken_distance


def solution(n, m, city):
    houses = []
    chickens = []
    for row in range(n):
        for col in range(n):
            if city[row][col] == 1:
                houses.append((row, col))
            if city[row][col] == 2:
                chickens.append((row, col))

    answer = int(1e9)
    candidates = list(combinations(chickens, m))
    for candidate in candidates:
        answer = min(answer, sum_chicken_distance(houses, candidate))
    return answer


if __name__ == '__main__':
    TESTCASE1 = [
        [0, 0, 1, 0, 0],
        [0, 0, 2, 0, 1],
        [0, 1, 2, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 2],
    ]
    TESTCASE2 = [
        [0, 2, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [2, 0, 0, 1, 1],
        [2, 2, 0, 1, 2],
    ]
    TESTCASE3 = [
        [1, 2, 0, 0, 0],
        [1, 2, 0, 0, 0],
        [1, 2, 0, 0, 0],
        [1, 2, 0, 0, 0],
        [1, 2, 0, 0, 0],
    ]
    TESTCASE4 = [
        [1, 2, 0, 2, 1],
        [1, 2, 0, 2, 1],
        [1, 2, 0, 2, 1],
        [1, 2, 0, 2, 1],
        [1, 2, 0, 2, 1],
    ]
    if solution(5, 3, TESTCASE1) == 5:
        print(f'TESTCASE 1 PASSED!')
    if solution(5, 2, TESTCASE2) == 10:
        print(f'TESTCASE 2 PASSED!')
    if solution(5, 1, TESTCASE3) == 11:
        print(f'TESTCASE 3 PASSED!')
    if solution(5, 1, TESTCASE4) == 32:
        print(f'TESTCASE 4 PASSED!')