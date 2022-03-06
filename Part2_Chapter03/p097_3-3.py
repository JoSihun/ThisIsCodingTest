def solution(cards):
    answers = []
    for row in cards:
        answers.append(min(row))
    return max(answers)



if __name__ == '__main__':
    TESTCASE1 = [
        [3, 1, 2],
        [4, 1, 4],
        [2, 2, 2]
    ]
    TESTCASE2 = [
        [7, 3, 1, 8],
        [3, 3, 3, 4]
    ]
    if solution(TESTCASE1) == 2:
        print(f'TESTCASE 1 PASSED!')
    if solution(TESTCASE2) == 3:
        print(f'TESTCASE 2 PASSED!')