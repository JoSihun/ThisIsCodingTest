def solution(array):
    answer = 0
    array.sort()
    group_member = 0
    for fear in array:
        group_member += 1
        if group_member >= fear:
            answer += 1
            group_member = 0

    return answer


if __name__ == '__main__':
    TESTCASE1 = [2, 3, 1, 2, 2]
    if solution(TESTCASE1) == 2:
        print(f'TESTCASE 1 PASSED!')