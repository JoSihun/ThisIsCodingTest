from collections import deque
def TopologySort(n, graph):
    indegree = [0] * (n + 1)
    for node_a in graph:
        for node_b in node_a:
            indegree[node_b] += 1

    answer = []
    q = deque()
    for node in range(1, n + 1):
        if indegree[node] == 0:
            q.append(node)
    while q:
        node_now = q.popleft()
        answer.append(node_now)
        for node in graph[node_now]:
            indegree[node] -= 1
            if indegree[node] == 0:
                q.append(node)
    return answer


if __name__ == '__main__':
    TESTCASE1 = [
        [],
        [2, 5],
        [3, 6],
        [4],
        [7],
        [6],
        [4],
        [],
    ]
    if TopologySort(7, TESTCASE1) == [1, 2, 5, 3, 6, 4, 7]:
        print(f'TESTCASE 1 PASSED!')