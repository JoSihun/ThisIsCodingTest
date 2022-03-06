# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def solution(arr, k):
    # k 이내 스왑 + 스왑 결과물에 대한 스코어링 + dfs..
    answer = 0
    while True:
        check = 0
        for i in range(len(arr)):
            if arr[i] == i + 1:
                check += 1
        if check == len(arr):
            break

        for idx in range(0, len(arr) - 1):
            for jdx in reversed(range(idx + 1, len(arr))):
                if jdx - idx <= k and arr[idx] > arr[jdx]:
                    temp = arr[idx]
                    arr[idx] = arr[jdx]
                    arr[jdx] = temp
                    answer += 1
                    break
    return answer




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    testcases = []
    testcase1 = [4, 5, 2, 3, 1]
    testcase2 = [5, 4, 3, 2, 1]
    testcase3 = [5, 4, 3, 2, 1]
    k1 = 2
    k2 = 4
    k3 = 2
    testcases.append(testcase1)

    answers = []
    answer1 = 4
    answer2 = 2
    answer3 = 4
    answers.append(answer1)

    for i, (testcase, answer) in enumerate(zip(testcases, answers)):
        user_answer = solution(testcase)
        if user_answer == answer:
            print(f'TESTCASE {i} PASSED')
        else:
            print(f'TESTCASE {i} FAILED')