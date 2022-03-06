def solution(s):
    char = ''.join(sorted([element for element in s if element.isalpha()]))
    sum_num = str(sum([int(num) for num in s if num.isnumeric()]))
    return char + sum_num


if __name__ == '__main__':
    if solution('K1KA5CB7') == 'ABCKK13':
        print(f'TESTCASE 1 PASSED!')
    if solution('AJKDLSI412K4JSJ9D') == 'ADDIJJJKKLSS20':
        print(f'TESTCASE 2 PASSED!')
