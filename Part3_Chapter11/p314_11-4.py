from itertools import combinations

# def solution(coins):
#     answer = [i for i in range(1, sum(coins) + 1)]
#     combination = set()
#     for n in range(1, len(coins) + 1):
#         for combi in list(combinations(coins, n)):
#             combination.add(sum(combi))
#     for combi in combination:
#         answer.remove(combi)
#
#     return min(answer)

def solution(coins):
    answer = 1
    for coin in sorted(coins):
        if answer < coin:
            return answer
        answer += coin


if __name__ == '__main__':
    if solution([3, 2, 1, 1, 9]) == 8:
        print(f'TESTCASE 1 PASSED!')
    if solution([3, 5, 7]) == 1:
        print(f'TESTCASE 2 PASSED!')
