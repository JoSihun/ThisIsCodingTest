INF = int(1e9)

def FloydWarshall(graph):
    n = len(graph)
    for k in range(n):
        for a in range(n):
            for b in range(n):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
    return graph

if __name__ == '__main__':
    TESTCASE1 = [
        [0, 4, INF, 6],
        [3, 0, 7, INF],
        [5, INF, 0, 4],
        [INF, INF, 2, 0]
    ]
    ANSWER = [
        [0, 4, 8, 6],
        [3, 0, 7, 9],
        [5, 9, 0, 4],
        [7, 11, 2, 0]
    ]
    if FloydWarshall(TESTCASE1) == ANSWER:
        print(f'TESTCASE 1 PASSED!')