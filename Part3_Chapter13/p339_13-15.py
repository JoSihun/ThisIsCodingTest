from collections import deque


def solution(n, m, k, x, graph):
    distance = [-1] * (n + 1)
    distance[x] = 0

    q = deque([x])
    while q:
        node_now = q.popleft()
        for node_next in graph[node_now]:
            if distance[node_next] == -1:
                distance[node_next] = distance[node_now] + 1
                q.append(node_next)

    answer = []
    for i in range(1, n + 1):
        if distance[i] == k:
            answer.append(i)

    return -1 if not answer else answer


if __name__ == '__main__':
    TESTCASE1 = [
        [],
        [2, 3],
        [3, 4],
        [],
        [],
    ]
    TESTCASE2 = [
        [],
        [2, 3, 4],
        [],
        [],
        [],
    ]
    TESTCASE3 = [
        [],
        [2, 3],
        [3, 4],
        [],
        [],
    ]
    if solution(4, 4, 2, 1, TESTCASE1) == [4]:
        print(f'TESTCASE 1 PASSED!')
    if solution(4, 3, 2, 1, TESTCASE2) == -1:
        print(f'TESTCASE 2 PASSED!')
    if solution(4, 4, 1, 1, TESTCASE3) == [2, 3]:
        print(f'TESTCASE 3 PASSED!')