from collections import deque
def solution(board, moves):
    answer = 0
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 상우하좌 시계방향순

    head_dir_now = 1
    tail_dir_now = 1
    snake_head = [0, 0]
    snake_tail = [0, 0]
    board[0][0] = 7
    dir_change_condition = deque()
    for move_sec, move_dir in moves:
        while answer != move_sec:
            answer += 1
            snake_head[0] += directions[head_dir_now][0]
            snake_head[1] += directions[head_dir_now][1]

            # 종료조건1: 벽에 부딫혔을 때
            if snake_head[0] < 0 or snake_head[0] > len(board) - 1:
                return answer
            if snake_head[1] < 0 or snake_head[1] > len(board) - 1:
                return answer
            # 종료조건2: 자기 몸에 부딫혔을 때
            if board[snake_head[0]][snake_head[1]] == 7:
                return answer

            # 사과가 없으면
            if board[snake_head[0]][snake_head[1]] == 0:
                board[snake_tail[0]][snake_tail[1]] = 0
                if snake_tail == dir_change_condition[0][0]:
                    if dir_change_condition[0][1] == 'L':
                        tail_dir_now = (tail_dir_now - 1) % 4
                    if dir_change_condition[0][1] == 'D':
                        tail_dir_now = (tail_dir_now + 1) % 4
                    dir_change_condition.popleft()
                snake_tail[0] += directions[tail_dir_now][0]
                snake_tail[1] += directions[tail_dir_now][1]
            board[snake_head[0]][snake_head[1]] = 7

            for row in board:
                print(row)
            print()

        if move_dir == 'L':
            dir_change_condition.append([snake_head, 'L'])
            head_dir_now = (head_dir_now - 1) % 4
        if move_dir == 'D':
            dir_change_condition.append([snake_head, 'D'])
            head_dir_now = (head_dir_now + 1) % 4
        print(dir_change_condition)


def solution(board, moves):
    answer = 0
    rotate = 0
    direction = 1
    dx = [-1, 0, 1, 0]  # 상우하좌 시계방향순
    dy = [0, 1, 0, -1]  # 상우하좌 시계방향순

    x, y = 0, 0
    board[x][y] = 7
    snake_q = deque([(x, y)])
    while True:
        answer += 1
        nx = x + dx[direction]
        ny = y + dy[direction]
        if not (-1 < nx < len(board) and -1 < ny < len(board)) or board[nx][ny] == 7:
            return answer

        if board[nx][ny] == 0:
            px, py = snake_q.popleft()
            board[px][py] = 0
        board[nx][ny] = 7
        snake_q.append((nx, ny))
        x, y = nx, ny
        if rotate < len(moves) and answer == moves[rotate][0]:
            if moves[rotate][1] == 'L':
                direction = (direction - 1) % 4
            if moves[rotate][1] == 'D':
                direction = (direction + 1) % 4
            rotate += 1


if __name__ == '__main__':
    TESTCASE1_BOARD = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]
    TESTCASE2_BOARD = [
        [0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    TESTCASE3_BOARD = [
        [0, 1, 1, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    TESTCASE1_MOVE = [[3, 'D'], [15, 'L'], [17, 'D']]
    TESTCASE2_MOVE = [[8, 'D'], [10, 'D'], [11, 'D'], [13, 'L']]
    TESTCASE3_MOVE = [[8, 'D'], [10, 'D'], [11, 'D'], [13, 'L']]
    if solution(TESTCASE1_BOARD, TESTCASE1_MOVE) == 9:
        print(f'TESTCASE 1 PASSED!')
    if solution(TESTCASE2_BOARD, TESTCASE2_MOVE) == 21:
        print(f'TESTCASE 2 PASSED!')
    if solution(TESTCASE3_BOARD, TESTCASE3_MOVE) == 13:
        print(f'TESTCASE 3 PASSED!')