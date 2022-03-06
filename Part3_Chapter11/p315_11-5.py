# def solution(balls):
#     answer = 0
#     for idx in range(len(balls) - 1):
#         for jdx in range(idx + 1, len(balls)):
#             if balls[idx] != balls[jdx]:
#                 answer += 1
#     return answer

def solution(balls):
    counts = [0] * (max(balls) + 1)
    for weight in balls:
        counts[weight] += 1

    answer = 0
    n = len(balls)
    for weight in range(1, max(balls) + 1):
        n -= counts[weight]
        answer += counts[weight] * n

    return answer


if __name__ == '__main__':
    if solution([1, 3, 2, 3, 2]) == 8:
        print(f'TESTCASE 1 PASSED!')
    if solution([1, 5, 4, 3, 2, 4, 5, 2]) == 25:
        print(f'TESTCASE 2 PASSED!')
