def solution(score):
    left, right = str(score)[:len(str(score)) // 2], str(score)[len(str(score)) // 2:]
    return 'LUCKY' if sum([int(num) for num in left]) == sum([int(num) for num in right]) else 'READY'


if __name__ == '__main__':
    if solution(123402) == 'LUCKY':
        print(f'TESTCASE 1 PASSED!')
    if solution(7755) == 'READY':
        print(f'TESTCASE 2 PASSED!')
