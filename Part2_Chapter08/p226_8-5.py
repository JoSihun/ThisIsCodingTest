def solution(m, money):
    answer = [10001] * (m + 1)
    answer[0] = 0
    for element in money:
        for i in range(element, m + 1):
            if answer[i - element] != 10001:
                answer[i] = min(answer[i], answer[i - element] + 1)

    return answer[m] if answer[m] != 10001 else -1

if __name__ == '__main__':
    TESTCASE1 = [2, 3]
    TESTCASE2 = [3, 5, 7]
    if solution(15, TESTCASE1) == 5:
        print(f'TESTCASE 1 PASSED!')
    if solution(4, TESTCASE2) == -1:
        print(f'TESTCASE 2 PASSED!')