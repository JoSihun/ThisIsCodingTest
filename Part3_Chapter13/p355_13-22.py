# https://programmers.co.kr/learn/courses/30/lessons/60063?language=python3#
from collections import deque

def get_next_pos(pos, board):
    next_pos = []   # 이동가능한 모든 위치
    pos = list(pos)
    x1, y1 = pos[0][0], pos[0][1]
    x2, y2 = pos[1][0], pos[1][1]
    dx = [-1, 1, 0, 0]  # 상하좌우순
    dy = [0, 0, -1, 1]  # 상하좌우순
    for i in range(4):  # 상하좌우 4개방향에 대해
        nx1, ny1 = x1 + dx[i], y1 + dy[i]
        nx2, ny2 = x2 + dx[i], y2 + dy[i]
        if board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
            next_pos.append({(nx1, ny1), (nx2, ny2)})
    if x1 == x2:    # 현재 로봇이 가로로 위치한 경우
        for i in [-1, 1]:   # 회전방향
            if board[x1 + i][y1] == 0 and board[x2 + i][y2] == 0:
                next_pos.append({(x1, y1), (x1 + i, y1)})
                next_pos.append({(x2, y2), (x2 + i, y2)})
    elif y1 == y2:  # 현재 로봇이 세로로 위치한 경우
        for i in [-1, 1]:   # 회전방향
            if board[x1][y1 + i] == 0 and board[x2][y2 + i] == 0:
                next_pos.append({(x1, y1), (x1, y1 + i)})
                next_pos.append({(x2, y2), (x2, y2 + i)})
    return next_pos



def solution(board):
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]

    q = deque()
    visited = []
    pos = {(1, 1), (1, 2)}
    q.append((pos, 0))
    visited.append(pos)
    while q:
        pos, cost = q.popleft()
        if (n, n) in pos:
            return cost
        for next_pos in get_next_pos(pos, new_board):
            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                visited.append(next_pos)

    return 0


if __name__ == '__main__':
    TESTCASE1 = [
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 1, 1],
        [1, 1, 0, 0, 1],
        [0, 0, 0, 0, 0],
    ]
    if solution(TESTCASE1) == 7:
        print(f'TESTCASE 1 PASSED!')
