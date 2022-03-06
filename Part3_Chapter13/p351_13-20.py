from itertools import combinations

def watch(x, y, array):
    temp_x, temp_y = x, y
    while 0 <= temp_x:
        if array[temp_x][temp_y] == 'S':
            return True
        if array[temp_x][temp_y] == 'O':
            break
        temp_x -= 1
    temp_x, temp_y = x, y
    while temp_x < len(array):
        if array[temp_x][temp_y] == 'S':
            return True
        if array[temp_x][temp_y] == 'O':
            break
        temp_x += 1
    temp_x, temp_y = x, y
    while 0 <= temp_y:
        if array[temp_x][temp_y] == 'S':
            return True
        if array[temp_x][temp_y] == 'O':
            break
        temp_y -= 1
    temp_x, temp_y = x, y
    while temp_y < len(array):
        if array[temp_x][temp_y] == 'S':
            return True
        if array[temp_x][temp_y] == 'O':
            break
        temp_y += 1
    return False


def solution(n, array):
    spaces = []
    teachers = []
    for i in range(n):
        for j in range(n):
            if array[i][j] == 'X':
                spaces.append((i, j))
            if array[i][j] == 'T':
                teachers.append((i, j))

    candidates = list(combinations(spaces, 3))
    for candidate in candidates:
        for x, y in candidate:
            array[x][y] = 'O'
        count = 0
        for x, y in teachers:
            if not watch(x, y, array):
                count += 1
        if count == len(teachers):
            return 'YES'
        for x, y in candidate:
            array[x][y] = 'X'

    return 'NO'


if __name__ == '__main__':
    TESTCASE1 = [
        ['X', 'S', 'X', 'X', 'T'],
        ['T', 'X', 'S', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X'],
        ['X', 'T', 'X', 'X', 'X'],
        ['X', 'X', 'T', 'X', 'X'],
    ]
    TESTCASE2 = [
        ['S', 'S', 'S', 'T'],
        ['X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X'],
        ['T', 'T', 'T', 'X'],
    ]
    if solution(5, TESTCASE1) == 'YES':
        print(f'TESTCASE 1 PASSED!')
    if solution(4, TESTCASE2) == 'NO':
        print(f'TESTCASE 2 PASSED!')