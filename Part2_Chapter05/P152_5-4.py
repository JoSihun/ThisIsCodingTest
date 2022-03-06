from collections import deque

def BFS(row, col, graph):
    queue = deque()
    queue.append((row, col))
    rows, cols = len(graph), len(graph[0])
    moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 상하좌우순
    while queue:
        row, col = queue.popleft()
        for idx in range(4):                    # 상하좌우확인
            next_row = row + moves[idx][0]
            next_col = col + moves[idx][1]
            # row, col 범위 벗어나는 경우
            if not -1 < next_row < rows or not -1 < next_col < cols:
                continue
            if graph[next_row][next_col] == 0:      # 괴물이 있는 경우
                continue
            if graph[next_row][next_col] == 1:      # 이동가능한 경우
                graph[next_row][next_col] = graph[row][col] + 1
                queue.append((next_row, next_col))
    return graph[-1][-1]

def solution(graph):
    answer = BFS(0, 0, graph)
    return answer


if __name__ == '__main__':
    TESTCASE1 = [
        [1, 0, 1, 0, 1, 0],
        [1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1]
    ]
    TESTCASE2 = [
        [1, 1, 0],
        [0, 1, 0],
        [0, 1, 1]
    ]
    if solution(TESTCASE1) == 10:
        print(f'TESTCASE 1 PASSED!')
    if solution(TESTCASE2) == 5:
        print(f'TESTCASE 2 PASSED!')