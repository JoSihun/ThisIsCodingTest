import heapq

def solution(start, graph):
    distance = [INF] * len(graph)
    distance[start] = 0

    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        dist_now, node_now = heapq.heappop(queue)
        if distance[node_now] < dist_now:
            continue
        for node, dist in graph[node_now]:
            cost = dist_now + dist
            if cost < distance[node]:
                distance[node] = cost
                heapq.heappush(queue, (cost, node))

    count = 0
    max_distance = 0
    for dist in distance:
        if dist != INF:
            count += 1
            max_distance = max(max_distance, dist)
    return [count - 1, max_distance]

INF = int(1e9)
if __name__ == '__main__':
    TESTCASE1 = [
        [],
        [(2, 4), (3, 2)],
        [],
        [],
    ]

    if solution(1, TESTCASE1) == [2, 4]:
        print(f'TESTCASE 1 PASSED!')