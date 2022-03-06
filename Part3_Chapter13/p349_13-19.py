from itertools import permutations

def solution(array, operators):
    opers = []
    for i in range(operators[0]):
        opers.append('+')
    for i in range(operators[1]):
        opers.append('-')
    for i in range(operators[2]):
        opers.append('x')
    for i in range(operators[3]):
        opers.append('/')

    answers = []
    operss = list(permutations(opers))
    for opers in operss:
        answer = array[0]
        for num, oper in zip(array[1:], opers):
            if oper == '+':
                answer = answer + num
            if oper == '-':
                answer = answer - num
            if oper == 'x':
                answer = answer * num
            if oper == '/':
                if answer < 0:
                    answer = -1 * ((-1 * answer) // num)
                else:
                    answer = answer // num
        answers.append(answer)
    return [max(answers), min(answers)]


if __name__ == '__main__':
    if solution([5, 6], [0, 0, 1, 0]) == [30, 30]:
        print(f'TESTCASE 1 PASSED!')
    if solution([3, 4, 5], [1, 0, 1, 0]) == [35, 17]:
        print(f'TESTCASE 2 PASSED!')
    if solution([1, 2, 3, 4, 5, 6], [2, 1, 1, 1]) == [54, -24]:
        print(f'TESTCASE 3 PASSED!')