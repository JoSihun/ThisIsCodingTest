def solution(player, array):
    moves = {0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]}
    rows, cols = len(array), len(array[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    p_row, p_col, p_dir = player
    visited[p_row][p_col] = True
    dir_cnt = 0
    while True:
        p_dir = (p_dir - 1) % 4
        next_row = p_row + moves[p_dir][0]
        next_col = p_col + moves[p_dir][1]

        if array[next_row][next_col] == 0 and visited[next_row][next_col] is False:  # 이동가능 + 가보지 않은지역
            p_row, p_col = next_row, next_col
            visited[p_row][p_col] = True
            dir_cnt = 0
        else:
            dir_cnt += 1
            if dir_cnt == 4:
                next_row = p_row - moves[p_dir][0]
                next_col = p_col - moves[p_dir][1]
                if array[next_row][next_col] == 1:
                    break
                p_row, p_col = next_row, next_col
                dir_cnt = 0

    answer = 0
    for row in range(rows):
        for col in range(cols):
            if visited[row][col] is True:
                answer += 1
    return answer

if __name__ == '__main__':
    TESTCASE1 = [
        [1, 1, 1, 1],
        [1, 0, 0, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 1]
    ]
    if solution([1, 1, 0], TESTCASE1) == 3:
        print(f'TESTCASE 1 PASSED!')