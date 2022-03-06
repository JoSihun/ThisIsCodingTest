def solution(n, k):
    answer = 0
    while n != 1:
        if n % k == 0:
            n = n / k
        else:
            n = n - 1
        answer += 1
    return answer

if __name__ == '__main__':
    if solution(17, 4) == 3:
        print(f'TESTCASE 1 PASSED!')
    if solution(25, 5) == 2:
        print(f'TESTCASE 2 PASSED!')