def Fibonacci(x):
    if x == 1 or x == 2:
        return 1
    return Fibonacci(x-1) + Fibonacci(x-2)

def Fibonacci_TopDown(x, memoization):
    if x == 1 or x == 2:
        return 1
    if memoization[x] != 0:
        return memoization[x]
    memoization[x] = Fibonacci_TopDown(x-1, memoization) + Fibonacci_TopDown(x-2, memoization)
    return memoization[x]

def Fibonacci_BottomUp(x):
    dp_table = [0] * 100
    dp_table[1] = 1
    dp_table[2] = 1
    for idx in range(3, x + 1):
        dp_table[idx] = dp_table[idx-1] + dp_table[idx-2]
    return dp_table[x]



if __name__ == '__main__':
    if Fibonacci(4) == 3:
        print(f'TESTCASE 1 PASSED!')

    memoization = [0] * 100
    if Fibonacci_TopDown(4, memoization) == 3:
        print(f'TESTCASE 2 PASSED!')

    if Fibonacci_BottomUp(4) == 3:
        print(f'TESTCASE 3 PASSED!')
