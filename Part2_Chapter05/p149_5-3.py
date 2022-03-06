def DFS(row, col, graph):
    rows, cols = len(graph), len(graph[0])
    if not -1 < row < rows or not -1 < col < cols:
        return False

    if graph[row][col] == 0:    # 방문하지 않았다면 새 아이스크림 존재
        graph[row][col] = 1         # 인접한 칸 전부 방문한 것으로 처리
        DFS(row - 1, col, graph)    # 상
        DFS(row + 1, col, graph)    # 하
        DFS(row, col - 1, graph)    # 좌
        DFS(row, col + 1, graph)    # 우
        return True             # 새 아이스크림 존재하기 때문에 return True
    return False                # 새 아이스크림 존재하지 않기 때문에 return False


def solution(graph):
    answer = 0
    rows, cols = len(graph), len(graph[0])

    for row in range(rows):
        for col in range(cols):
            if DFS(row, col, graph) == True:
                answer += 1
    return answer


if __name__ == '__main__':
    TESTCASE1 = [
        [0, 0, 1, 1, 0],
        [0, 0, 0, 1, 1],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0]
    ]
    TESTCASE2 = [
        [0, 0, 1],
        [0, 1, 0],
        [1, 0, 1]
    ]
    TESTCASE3 = [
        [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
        [1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

    if solution(TESTCASE1) == 3:
        print(f'TESTCASE 1 PASSED!')
    if solution(TESTCASE2) == 3:
        print(f'TESTCASE 2 PASSED!')
    if solution(TESTCASE3) == 8:
        print(f'TESTCASE 3 PASSED!')
