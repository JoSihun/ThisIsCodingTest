def solution(numbers):
    numbers = [int(i) for i in numbers]
    count_group = [0, 0]
    count_group[numbers[0]] += 1
    for idx in range(1, len(numbers)):
        if numbers[idx - 1] != numbers[idx]:
            count_group[numbers[idx]] += 1

    return min(count_group)


if __name__ == '__main__':
    if solution('0001100') == 1:
        print(f'TESTCASE 1 PASSED!')
    if solution('1000110001') == 2:
        print(f'TESTCASE 2 PASSED!')
