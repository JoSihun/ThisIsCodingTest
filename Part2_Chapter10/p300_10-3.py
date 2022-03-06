def find_parent(x, parent):
    if parent[x] != x:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]

def union_parent(a, b, parent):
    a = find_parent(a, parent)
    b = find_parent(b, parent)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, graph):
    answer = 0
    edges = []
    parent = [i for i in range(n + 1)]

    for a, b, cost in graph:
        edges.append((cost, a, b))
    edges.sort()

    max_edge = 0
    for cost, a, b in edges:
        if find_parent(a, parent) != find_parent(b, parent):
            union_parent(a, b, parent)
            answer += cost
            max_edge = cost

    return answer - max_edge


if __name__ == '__main__':
    TESTCASE1 = [
        [1, 2, 3],
        [1, 3, 2],
        [3, 2, 1],
        [2, 5, 2],
        [3, 4, 4],
        [7, 3, 6],
        [5, 1, 5],
        [1, 6, 2],
        [6, 4, 1],
        [6, 5, 3],
        [4, 6, 3],
        [6, 7, 4],
    ]
    if solution(7, TESTCASE1) == 8:
        print(f'TESTCASE 1 PASSED!')