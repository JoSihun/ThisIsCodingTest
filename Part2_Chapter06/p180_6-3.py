def solution(array):
    answer = [element[0] for element in sorted(array, key=lambda x: x[1])]
    return answer

if __name__ == '__main__':
    TESTCASE1 = [
        ['홍길동', 95],
        ['이순신', 77]
    ]
    if solution(TESTCASE1) == ['이순신', '홍길동']:
        print(f'TESTCASE 1 PASSED!')
