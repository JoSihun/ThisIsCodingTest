def solution1(n, moves):
    answer = [1, 1]
    for move in moves:
        if answer[1] > 1 and move == 'L':
            answer[1] -= 1
        if answer[1] < n and move == 'R':
            answer[1] += 1
        if answer[0] > 1 and move == 'U':
            answer[0] -= 1
        if answer[0] < n and move == 'D':
            answer[0] += 1
    return answer

def solution2(n):
    answer = 0
    for h in range(n + 1):
        for m in range(60):
            for s in range(60):
                if '3' in str(s) + str(m) + str(h):
                    answer += 1
    return answer

if __name__ == '__main__':
    # 상하좌우
    if solution1(5, ['R', 'R', 'R', 'U', 'D', 'D']) == [3, 4]:
        print(f'TESTCASE 1 PASSED!')

    # 시각
    if solution2(5) == 11475:
        print(f'TESTCASE 2 PASSED!')