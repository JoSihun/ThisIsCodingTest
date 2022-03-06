# https://programmers.co.kr/learn/courses/30/lessons/42891?language=python3
import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for idx, time in enumerate(food_times):
        heapq.heappush(q, (time, idx + 1))

    sorted(q)
    sum_used_time = 0
    pre_used_time = 0
    num_left_food = len(food_times)
    while sum_used_time + (q[0][0] - pre_used_time) * num_left_food <= k:
        time_now, food_now = heapq.heappop(q)
        sum_used_time += (time_now - pre_used_time) * num_left_food
        num_left_food -= 1
        pre_used_time = time_now

    answer = sorted(q, key=lambda x: x[1])
    return answer[(k - sum_used_time) % num_left_food][1]

# # 오답
# def solution(k, food_times):
#     answer = 0
#     for _ in range(k):
#         if food_times[answer] == 0:
#             answer = (answer + 1) % len(food_times)
#         food_times[answer] -= 1
#         answer = (answer + 1) % len(food_times)
#     return answer + 1


if __name__ == '__main__':
    if solution([3, 1, 2], 5) == 1:
        print(f'TESTCASE 1 PASSED!')
    if solution([3, 1, 2, 4, 2], 11) == 4:
        print(f'TESTCASE 2 PASSED!')
