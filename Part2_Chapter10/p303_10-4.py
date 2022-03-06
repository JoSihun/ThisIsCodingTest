from collections import deque
import copy

def solution(n, time, graph):
    answer = 0
    indegree = [0] * (n + 1)
    for data in graph:
        for node in data:
            indegree[node] += 1

    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    answer = copy.deepcopy(time)
    while q:
        node_now = q.popleft()
        for node in graph[node_now]:
            answer[node] = max(answer[node], answer[node_now] + time[node])
            indegree[node] -= 1
            if indegree[node] == 0:
                q.append(node)

    return answer[1:]


if __name__ == '__main__':
    TIME = [0, 10, 10, 4, 4, 3]
    TESTCASE1 = [
        [],
        [2, 3, 4],
        [],
        [4, 5],
        [],
        [],
    ]
    if solution(5, TIME, TESTCASE1) == [10, 20, 14, 18, 17]:
        print(f'TESTCASE 1 PASSED!')