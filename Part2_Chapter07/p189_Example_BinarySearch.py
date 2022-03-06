def binary_search1(target, start, end, array):
    if start > end:
        return None

    mid = (start + end) // 2
    if array[mid] == target:
        return mid + 1
    elif array[mid] > target:
        return binary_search1(target, start, mid - 1, array)
    else:
        return binary_search1(target, mid + 1, end, array)

def binary_search2(target, start, end, array):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid + 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


if __name__ == '__main__':
    TESTCASE1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    TESTCASE2 = [1, 3, 5, 6, 9, 11, 13, 15, 17, 19]

    if binary_search1(7, 0, len(TESTCASE1)-1, TESTCASE1) == 4:
        print(f'TESTCASE 1 PASSED!')
    if binary_search1(7, 0, len(TESTCASE2)-1, TESTCASE2) == None:
        print(f'TESTCASE 2 PASSED!')

    if binary_search2(7, 0, len(TESTCASE1)-1, TESTCASE1) == 4:
        print(f'TESTCASE 1 PASSED!')
    if binary_search2(7, 0, len(TESTCASE2)-1, TESTCASE2) == None:
        print(f'TESTCASE 2 PASSED!')