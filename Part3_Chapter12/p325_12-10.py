# https://programmers.co.kr/learn/courses/30/lessons/60059?language=python3
import copy


def rotate(key):
    copy_key = copy.deepcopy(key)
    rows, cols = len(key), len(key[0])
    for row in range(rows):
        for col in range(cols):
            copy_key[row][col] = key[cols - 1 - col][row]
    return copy_key


def check_key(key, new_lock):
    n, m = len(new_lock), len(key)
    for x in range(n // 3 * 2):
        for y in range(n // 3 * 2):
            copy_lock = copy.deepcopy(new_lock)
            for i in range(m):
                for j in range(m):
                    copy_lock[x + i][y + j] += key[i][j]
            if check_lock(copy_lock):
                return True
    return False


def check_lock(new_lock):
    n_new_lock = len(new_lock) // 3
    for row in range(n_new_lock, n_new_lock * 2):
        for col in range(n_new_lock, n_new_lock * 2):
            if new_lock[row][col] != 1:
                return False
    return True


def solution(key, lock):
    n, m = len(lock), len(key)
    copy_lock = [[0] * (n * 3) for _ in range(n * 3)]
    for row in range(n):
        for col in range(n):
            copy_lock[row + n][col + n] = lock[row][col]

    for _ in range(4):
        key = rotate(key)
        if check_key(key, copy_lock):
            return True

    return False


if __name__ == '__main__':
    KEY = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    LOCK = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

    if solution(KEY, LOCK) == True:
        print(f'TESTCASE 1 PASSED!')