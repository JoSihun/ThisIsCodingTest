def solution(graph):
    answer = 0
    n, m = len(graph), len(graph[0])
    temp = [[0] * m for _ in range(n)]
    answer = DFS(temp, graph, 0, answer)
    print(answer)
    return answer

def virus(x, y, temp):
    dx = [0, 0, -1, 1]  # 상하좌우순
    dy = [-1, 1, 0, 0]  # 상하좌우순
    n, m = len(temp), len(temp[0])
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if -1 < nx < n and -1 < ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny, temp)

def get_score(temp):
    score = 0
    n, m = len(temp), len(temp[0])
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

def DFS(temp, graph, count, answer):
    n, m = len(graph), len(graph[0])
    # 벽이 3개가 다 세워졌다면
    if count == 3:
        # temp에 graph 복사
        for i in range(n):
            for j in range(m):
                temp[i][j] = graph[i][j]
        # 복사한 temp에서 바이러스 전파 시뮬레이션
        for i in range(n):
            for j in range(m):
                virus(i, j, temp)
        answer = max(answer, get_score(temp))
        return answer

    # 3개의 벽을 세우는 모든 경우의 수
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                DFS(temp, graph, count, answer)
                graph[i][j] = 0
                count -= 1

if __name__ == '__main__':
    TESTCASE1 = [
        [2, 0, 0, 0, 1, 1, 0],
        [0, 0, 1, 0, 1, 2, 0],
        [0, 1, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
    ]
    TESTCASE2 = [
        [0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 2],
        [1, 1, 1, 0, 0, 2],
        [0, 0, 0, 0, 0, 2],
    ]
    TESTCASE3 = [
        [2, 0, 0, 0, 0, 0, 0, 2],
        [2, 0, 0, 0, 0, 0, 0, 2],
        [2, 0, 0, 0, 0, 0, 0, 2],
        [2, 0, 0, 0, 0, 0, 0, 2],
        [2, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]
    if solution(TESTCASE1) == 27:
        print(f'TESTCASE 1 PASSED!')
    if solution(TESTCASE2) == 9:
        print(f'TESTCASE 2 PASSED!')
    if solution(TESTCASE3) == 3:
        print(f'TESTCASE 3 PASSED!')
