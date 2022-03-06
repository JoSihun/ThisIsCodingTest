def solution(pos):
    answer = 0
    col, row = pos

    # 수평 2회 이동
    if int(row) + 1 < 9 and ord(col) - 2 > ord('a') - 1:
        answer += 1
    if int(row) + 1 < 9 and ord(col) + 2 < ord('h') + 1:
        answer += 1
    if int(row) - 1 > 0 and ord(col) - 2 > ord('a') - 1:
        answer += 1
    if int(row) - 1 > 0 and ord(col) + 2 < ord('h') + 1:
        answer += 1

    # 수직 2회 이동
    if int(row) + 2 < 9 and ord(col) - 1 > ord('a') - 1:
        answer += 1
    if int(row) + 2 < 9 and ord(col) + 1 < ord('h') + 1:
        answer += 1
    if int(row) - 2 > 0 and ord(col) - 1 > ord('a') - 1:
        answer += 1
    if int(row) - 2 > 0 and ord(col) + 1 < ord('h') + 1:
        answer += 1

    return answer

if __name__ == '__main__':
    if solution('a1') == 2:
        print(f'TESTCASE 1 PASSED!')