from collections import deque

def solution(n, l, r, graph):
    answer = 0
    dx = [-1, 1, 0, 0]  # 상하좌우순
    dy = [0, 0, -1, 1]  # 상하좌우순

    while True:
        index = 0
        union = [[-1] * n for _ in range(n)]
        for idx in range(n):
            for jdx in range(n):
                if union[idx][jdx] == -1:
                    united = []
                    united.append((idx, jdx))
                    q = deque()
                    q.append((idx, jdx))
                    union[idx][jdx] = index
                    summary = graph[idx][jdx]
                    count = 1
                    while q:
                        x, y = q.popleft()
                        for direction in range(4):
                            nx = x + dx[direction]
                            ny = y + dy[direction]
                            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                                if l <= abs(graph[x][y] - graph[nx][ny]) <= r:
                                    q.append((nx, ny))
                                    union[nx][ny] = index
                                    summary += graph[nx][ny]
                                    count += 1
                                    united.append((nx, ny))
                    for x, y in united:
                        graph[x][y] = summary // count
                    index += 1
        if index == n * n:
            break
        answer += 1

    return answer


if __name__ == '__main__':
    TESTCASE1 = [
        [50, 30],
        [20, 40],
    ]
    TESTCASE2 = [
        [50, 30],
        [20, 40],
    ]
    TESTCASE3 = [
        [50, 30],
        [30, 40],
    ]
    TESTCASE4 = [
        [10, 15, 20],
        [20, 30, 25],
        [40, 22, 10],
    ]
    TESTCASE5 = [
        [10, 100, 20, 90],
        [80, 100, 60, 70],
        [70, 20, 30, 40],
        [50, 20, 100, 10],
    ]
    if solution(2, 20, 50, TESTCASE1) == 1:
        print(f'TESTCASE 1 PASSED!')
    if solution(2, 40, 50, TESTCASE2) == 0:
        print(f'TESTCASE 2 PASSED!')
    if solution(2, 20, 50, TESTCASE3) == 1:
        print(f'TESTCASE 3 PASSED!')
    if solution(3, 5, 10, TESTCASE4) == 2:
        print(f'TESTCASE 4 PASSED!')
    if solution(4, 10, 50, TESTCASE5) == 3:
        print(f'TESTCASE 5 PASSED!')
