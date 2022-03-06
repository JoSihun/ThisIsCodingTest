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
    answer = []
    parent = [i for i in range(n + 1)]
    for op, a, b in graph:
        if op == 0:
            union_parent(a, b, parent)
        elif op == 1:
            if find_parent(a, parent) == find_parent(b, parent):
                answer.append('YES')
            else:
                answer.append('NO')

    return ' '.join(answer)


if __name__ == '__main__':
    TESTCASE1 = [
        [0, 1, 3],
        [1, 1, 7],
        [0, 7, 6],
        [1, 7, 1],
        [0, 3, 7],
        [0, 4, 2],
        [0, 1, 1],
        [1, 1, 1],
    ]
    if solution(7, TESTCASE1) == 'NO NO YES':
        print(f'TESTCASE 1 PASSED!')