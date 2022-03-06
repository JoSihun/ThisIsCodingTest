# https://programmers.co.kr/learn/courses/30/lessons/60057?language=python3
def solution(s):
    answer = len(s)
    for step in range(1, len(s) // 2 + 1):
        count = 1
        compress = ''
        pre_letter = s[0:step]
        for i in range(step, len(s), step):
            if pre_letter == s[i:i + step]:
                count += 1
            else:
                compress += str(count) + pre_letter if count >= 2 else pre_letter
                pre_letter = s[i:i + step]
                count = 1
        compress += str(count) + pre_letter if count >= 2 else pre_letter
        answer = min(answer, len(compress))

    return answer


if __name__ == '__main__':
    if solution('aabbaccc') == 7:
        print(f'TESTCASE 1 PASSED!')
    if solution('ababcdcdababcdcd') == 9:
        print(f'TESTCASE 2 PASSED!')
    if solution('abcabcdede') == 8:
        print(f'TESTCASE 3 PASSED!')
    if solution('abcabcabcabcdededededede') == 14:
        print(f'TESTCASE 4 PASSED!')
    if solution('xababcdcdababcdcd') == 17:
        print(f'TESTCASE 5 PASSED!')
