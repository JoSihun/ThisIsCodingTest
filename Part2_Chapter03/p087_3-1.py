def answer_check():
    TESTCASE = [1260]
    ANSWERS = [6]
    for idx, (param, answer) in enumerate(zip(TESTCASE, ANSWERS)):
        if answer == solution(param):
            print(f'TESTCASE {idx} PASSED!')
        else:
            print(f'TESTCASE {idx} FAILED!')

def solution(n):
    answer = 0
    coins = [500, 100, 50, 10]
    for coin in coins:
        answer += n // coin
        n = n % coin
    return answer

if __name__ == '__main__':
    answer_check()