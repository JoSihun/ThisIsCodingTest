# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def solution(grid):
    cur_sum = 0
    path_sums = []
    DFS(0, 0, cur_sum, path_sums, grid)
    return min(path_sums)

def DFS(idx, jdx, cur_sum, path_sums, grid):
    cur_sum += grid[idx][jdx]
    if jdx < len(grid[0]) - 1:
        DFS(idx, jdx + 1, cur_sum, path_sums, grid)
    if idx < len(grid) - 1:
        DFS(idx + 1, jdx, cur_sum, path_sums, grid)
    if idx == len(grid) - 1 and jdx == len(grid[0]) - 1:
        path_sums.append(cur_sum)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    testcases = []
    testcase1 = [[1, 2], [3, 4]]
    testcase2 = [[1, 8, 3, 2], [7, 4, 6, 5]]
    testcases.append(testcase1)
    testcases.append(testcase2)

    answers = []
    answer1 = 7
    answer2 = 19
    answers.append(answer1)
    answers.append(answer2)

    for i, (testcase, answer) in enumerate(zip(testcases, answers)):
        user_answer = solution(testcase)
        if user_answer == answer:
            print(f'TESTCASE {i} PASSED')
        else:
            print(f'TESTCASE {i} FAILED')