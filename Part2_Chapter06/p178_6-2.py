def solution(array):
    answer = sorted(array, reverse=True)
    return answer

if __name__ == '__main__':
    TESTCASE1 = [15, 27, 12]
    if solution(TESTCASE1) == [27, 15, 12]:
        print(f'TESTCASE 1 PASSED!')
