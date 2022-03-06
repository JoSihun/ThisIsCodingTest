def solution(x, k, graph):
    n = len(graph)
    for l in range(n):
        for a in range(n):
            for b in range(n):
                graph[a][b] = min(graph[a][b], graph[a][l] + graph[l][b])

    answer = graph[0][k-1] + graph[k-1][x-1]
    return -1 if answer >= INF else answer

INF = int(1e9)
if __name__ == '__main__':
    TESTCASE1 = [
        [INF, 1, 1, 1, INF],
        [1, INF, INF, 1, INF],
        [1, INF, INF, 1, 1],
        [1, 1, 1, INF, 1],
        [INF, INF, 1, 1, INF],
    ]
    TESTCASE2 = [
        [INF, INF, 1, INF],
        [INF, INF, INF, 1],
        [1, INF, INF, INF],
        [INF, 1, INF, INF]
    ]
    if solution(4, 5, TESTCASE1) == 3:
        print(f'TESTCASE 1 PASSED!')
    if solution(3, 4, TESTCASE2) == -1:
        print(f'TESTCASE 2 PASSED!')