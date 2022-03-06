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

def Kruskal(n, graph):
    answer = 0
    edges = []
    parent = [i for i in range(n + 1)]

    for a, b, cost in graph:
        edges.append((cost, a, b))

    edges.sort()
    for cost, a, b in edges:
        if find_parent(a, parent) != find_parent(b, parent):
            union_parent(a, b, parent)
            answer += cost

    return answer

if __name__ == '__main__':
    TESTCASE1 = [
        [1, 2, 29],
        [1, 5, 75],
        [2, 3, 35],
        [2, 6, 34],
        [3, 4, 7],
        [4, 6, 23],
        [4, 7, 13],
        [5, 6, 53],
        [6, 7, 25],
    ]
    if Kruskal(7, TESTCASE1) == 159:
        print(f'TESTCASE 1 PASSED!')