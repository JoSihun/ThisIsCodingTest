def solution(x):
    answer = [0] * 50
    for i in range(2, x + 1):
        answer[i] = answer[i-1] + 1
        if i % 2 == 0:
            answer[i] = min(answer[i], answer[i // 2] + 1)
        if i % 3 == 0:
            answer[i] = min(answer[i], answer[i // 3] + 1)
        if i % 5 == 0:
            answer[i] = min(answer[i], answer[i // 5] + 1)
        print(answer)
    return answer[x]

if __name__ == '__main__':
    if solution(26) == 3:
        print(f'TESTCASE 1 PASSED!')