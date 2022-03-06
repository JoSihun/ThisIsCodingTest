def solution(n, k, array1, array2):
    array1.sort()
    array2.sort(reverse=True)
    for idx in range(k):
        if array1[idx] < array2[idx]:
            array1[idx], array2[idx] = array2[idx], array1[idx]
        else:
            break
    return sum(array1)

if __name__ == '__main__':
    TESTCASE1_array1 = [1, 2, 5, 4, 3]
    TESTCASE1_array2 = [5, 5, 6, 6, 5]
    if solution(5, 3, TESTCASE1_array1, TESTCASE1_array2) == 26:
        print(f'TESTCASE 1 PASSED!')