import heapq

def dijkstra(graph):
    distance = [int(1e9)] * len(graph)

    queue = []
    distance[1] = 0
    heapq.heappush(queue, (0, 1))
    while queue:
        dist_now, node_now = heapq.heappop(queue)
        if distance[node_now] < dist_now:
            continue
        for node, dist in graph[node_now]:
            # print(node, dist)
            cost = dist_now + dist
            if cost < distance[node]:
                distance[node] = cost
                heapq.heappush(queue, (cost, node))

    return distance[1:]


if __name__ == '__main__':
    TESTCASE1 = [
        [],
        [(2, 2), (3, 5), (4, 1)],
        [(3, 3), (4, 2)],
        [(2, 3), (6, 5)],
        [(3, 3), (5, 1)],
        [(3, 1), (6, 2)],
        []
    ]
    # 테스트케이스 형태가 이상함, 책보고 그대로 작성한다음 출력해볼것
    if dijkstra(TESTCASE1) == [0, 2, 3, 1, 2, 4]:
        print(f'TESTCASE 1 PASSED!')