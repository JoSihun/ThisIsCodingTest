def solution(numbers):
    answer = int(numbers[0])
    for idx in range(1, len(numbers)):
        if answer == 0 or numbers[idx] == str(0):
            answer += int(numbers[idx])
        else:
            answer *= int(numbers[idx])

    return answer


if __name__ == '__main__':
    if solution('02984') == 576:
        print(f'TESTCASE 1 PASSED!')
    if solution('567') == 210:
        print(f'TESTCASE 2 PASSED!')