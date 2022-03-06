import heapq

def solution(s, x, y, graph):
    n = len(graph)
    heap = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                heapq.heappush(heap, (graph[i][j], i, j))

    dr = [-1, 1, 0, 0]  # 상하좌우순
    dc = [0, 0, -1, 1]  # 상하좌우순
    for _ in range(s):
        temp = []
        length = len(heap)
        for _ in range(length):
            virus, row, col = heapq.heappop(heap)
            for i in range(4):
                nr = row + dr[i]
                nc = col + dc[i]
                if -1 < nr < n and -1 < nc < n and graph[nr][nc] == 0:
                    graph[nr][nc] = virus
                    heapq.heappush(temp, (virus, nr, nc))
        heap = temp
    
    return graph[x - 1][y - 1]


if __name__ == '__main__':
    TESTCASE1 = [
        [1, 0, 2],
        [0, 0, 0],
        [3, 0, 0],
    ]
    TESTCASE2 = [
        [1, 0, 2],
        [0, 0, 0],
        [3, 0, 0],
    ]
    if solution(2, 3, 2, TESTCASE1) == 3:
        print(f'TESTCASE 1 PASSED!')
    if solution(1, 2, 2, TESTCASE2) == 0:
        print(f'TESTCASE 2 PASSED!')