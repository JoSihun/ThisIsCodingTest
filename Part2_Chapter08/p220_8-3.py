def solution(array):
    answer = [0] * 100
    answer[0] = array[0]
    answer[1] = max(array[0], array[1])
    for i in range(2, len(array)):
        answer[i] = max(answer[i-2] + array[i], answer[i-1])
    return answer[len(array)-1]

if __name__ == '__main__':
    TESTCASE1 = [1, 3, 1, 5]
    if solution(TESTCASE1) == 8:
        print(f'TESTCASE 1 PASSED!')