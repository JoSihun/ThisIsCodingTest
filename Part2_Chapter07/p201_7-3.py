def solution(target, array):
    answer = 0

    start = 0
    end = max(array)
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for element in array:
            if element > mid:
                total += element - mid
        if total < target:
            end = mid - 1
        else:
            start = mid + 1
            answer = mid

    return answer

if __name__ == '__main__':
    TESTCASE1 = [19, 15, 10, 17]
    if solution(6, TESTCASE1) == 15:
        print(f'TESTCASE 1 PASSED!')