# https://programmers.co.kr/learn/courses/30/lessons/60061?language=python3

# 오답
# def solution(n, build_frame):
#     answer = []
#     architecture = [[0] * (n + 1) for _ in range(n + 1)]
#
#     for x, y, a, b in build_frame:
#         if a == 0:  # 기둥
#             if b == 0:  # 삭제
#                 architecture[n - y][x] = 0
#                 architecture[n - y - 1][x] = 0
#             if b == 1:  # 설치
#                 if y == 0 or architecture[n - y][x] > 0:
#                     architecture[n - y][x] = 1
#                     architecture[n - y - 1][x] = 1
#         if a == 1:  # 보
#             if b == 0:  # 삭제
#                 architecture[n - y][x] = 0
#                 architecture[n - y][x + 1] = 0
#             if b == 1:  # 설치
#                 if architecture[n - y][x] > 0 or architecture[n - y][x + 1] > 0:
#                     architecture[n - y][x] = 2
#                     architecture[n - y][x + 1] = 2
#
#     for row in range(n + 1):
#         for col in range(n + 1):
#             if architecture[row][col] == 1:
#                 answer.append([col, n - row, 0])
#             if architecture[row][col] == 2:
#                 answer.append([col, n - row, 1])
#
#     return sorted(answer)[:-1]

def possible(answer):
    for x, y, architecture in answer:
        if architecture == 0:   # 기둥
            # 바닥위, 보의 한쪽 끝부분 위, 다른 기둥 위
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False
        if architecture == 1:   # 보
            # 한쪽 끝부분이 기둥 위, 양쪽 끝부분이 다른보와 동시에 연결
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    for x, y, architecture, operate in build_frame:
        if operate == 0:    # 삭제
            answer.remove([x, y, architecture])
            if not possible(answer):
                answer.append([x, y, architecture])
        if operate == 1:    # 설치
            answer.append([x, y, architecture])
            if not possible(answer):
                answer.remove([x, y, architecture])
    return sorted(answer)


if __name__ == '__main__':
    TESTCASE1 = [
        [1, 0, 0, 1],
        [1, 1, 1, 1],
        [2, 1, 0, 1],
        [2, 2, 1, 1],
        [5, 0, 0, 1],
        [5, 1, 0, 1],
        [4, 2, 1, 1],
        [3, 2, 1, 1],
    ]
    TESTCASE2 = [
        [0, 0, 0, 1],
        [2, 0, 0, 1],
        [4, 0, 0, 1],
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [2, 1, 1, 1],
        [3, 1, 1, 1],
        [2, 0, 0, 0],
        [1, 1, 1, 0],
        [2, 2, 0, 1],
    ]
    ANSWER1 = [
        [1, 0, 0],
        [1, 1, 1],
        [2, 1, 0],
        [2, 2, 1],
        [3, 2, 1],
        [4, 2, 1],
        [5, 0, 0],
        [5, 1, 0],
    ]
    ANSWER2 = [
        [0, 0, 0],
        [0, 1, 1],
        [1, 1, 1],
        [2, 1, 1],
        [3, 1, 1],
        [4, 0, 0],
    ]
    if solution(5, TESTCASE1) == ANSWER1:
        print(f'TESTCASE 1 PASSED!')
    if solution(5, TESTCASE2) == ANSWER2:
        print(f'TESTCASE 2 PASSED!')