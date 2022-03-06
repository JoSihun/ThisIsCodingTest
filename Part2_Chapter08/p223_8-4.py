def solution(n):
    answer = [0] * (n + 1)
    answer[1] = 1
    answer[2] = 3
    for i in range(3, n + 1):
        answer[i] = (answer[i-1] + answer[i-2] * 2) % 796796
    return answer[n]

if __name__ == '__main__':
    if solution(3) == 5:
        print(f'TESTCASE 1 PASSED!')