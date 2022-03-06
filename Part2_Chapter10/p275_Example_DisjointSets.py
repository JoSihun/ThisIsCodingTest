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
    return parent

def DisjointSets(n, graph):
    parent = [i for i in range(n + 1)]
    for a, b in graph:
        union_parent(a, b, parent)
    for node in range(1, n + 1):
        find_parent(node, parent)
    return parent[1:]

def CycleCheck(n, graph):
    cycle = False
    parent = [i for i in range(n + 1)]
    for a, b in graph:
        if find_parent(a, parent) == find_parent(b, parent):
            cycle = True
            break
        else:
            union_parent(a, b, parent)
    return cycle

if __name__ == '__main__':
    TESTCASE1 = [
        [1, 4],
        [2, 3],
        [2, 4],
        [5, 6],
    ]
    TESTCASE2 = [
        [1, 2],
        [1, 3],
        [2, 3],
    ]
    if DisjointSets(6, TESTCASE1) == [1, 1, 1, 1, 5, 5]:
        print(f'TESTCASE 1 PASSED!')
    if CycleCheck(3, TESTCASE2) == True:
        print(f'TESTCASE 2 PASSED!')