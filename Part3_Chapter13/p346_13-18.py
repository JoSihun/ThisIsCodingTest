# https://programmers.co.kr/learn/courses/30/lessons/60058?language=python3

def divide(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        elif p[i] == ')':
            count -= 1
        if count == 0:
            return p[:i + 1], p[i + 1:]


def check(p):
    count = 0
    for char in p:
        if char == '(':
            count += 1
        elif char == ')':
            if count == 0:
                return False
            count -= 1
    return True


def solution(p):
    answer = ''
    if p == '':
        return answer
    u, v = divide(p)
    if check(u):
        answer = u + solution(v)
    else:
        answer = '(' + solution(v) + ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer = answer + ''.join(u)
    return answer


if __name__ == '__main__':
    if solution('(()())()') == '(()())()':
        print(f'TESTCASE 1 PASSED!')
    if solution(')(') == '()':
        print(f'TESTCASE 2 PASSED!')
    if solution('()))((()') == '()(())()':
        print(f'TESTCASE 3 PASSED!')