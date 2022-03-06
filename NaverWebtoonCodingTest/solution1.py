# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def solution(lottery):
    checkDict1 = dict()
    for userId, check in lottery:
        if not userId in checkDict1 and check == 1:
            checkDict1[userId] = 0
    if len(checkDict1) == 0:
        return 0

    checkDict2 = dict()
    for userId in checkDict1.keys():
        if not userId in checkDict2:
            checkDict2[userId] = False

    for userId, check in lottery:
        if userId in checkDict2:
            if checkDict2[userId] == False:
                checkDict1[userId] += 1
                if check == 1:
                    checkDict2[userId] = True

    sum = 0
    for value in checkDict1.values():
        sum += value
    answer = sum // len(checkDict1)

    return answer




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    testcases = []
    testcase1 = [[1, 0], [35, 0], [1, 0], [100, 1], [35, 1], [100, 1], [35, 0], [1, 1], [1, 1]]
    testcase2 = [[1, 0], [2, 0], [3, 0], [1, 0], [2, 0], [1, 0], [1, 1], [2, 0], [2, 0], [2, 1], [1, 0], [1, 1], [3, 0], [3, 0], [1, 1]]
    testcase3 = [[1, 0], [2, 0], [3, 0]]
    testcases.append(testcase1)
    testcases.append(testcase2)
    testcases.append(testcase3)

    answers = []
    answer1 = 2
    answer2 = 4
    answer3 = 0
    answers.append(answer1)
    answers.append(answer2)
    answers.append(answer3)

    for i, (testcase, answer) in enumerate(zip(testcases, answers)):
        user_answer = solution(testcase)
        if user_answer == answer:
            print(f'TESTCASE {i} PASSED')
        else:
            print(f'TESTCASE {i} FAILED')