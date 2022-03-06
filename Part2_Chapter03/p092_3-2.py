def solution(n, m, k):
    answer = 0
    n.sort()

    cnt = 0
    for idx in range(m):
        if cnt < k:
            cnt += 1
            answer += n[-1]
        else:
            cnt = 0
            answer += n[-2]

    return answer

def solution2(n, m, k):
    n.sort()
    count = (m // (k + 1)) * k + m % (k + 1)
    answer = count * n[-1] + (m - count) * n[-2]

    return answer

if __name__ == '__main__':
    if solution([2, 4, 5, 4, 6], 8, 3) == 46:
        print(f'TESTCASE 1 PASSED!')
    if solution2([2, 4, 5, 4, 6], 8, 3) == 46:
        print(f'TESTCASE 1 PASSED!')