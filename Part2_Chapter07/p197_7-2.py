def binary_search(target, start, end, array):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        if array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None

def solution(customer, store):
    answer = []
    for custom in customer:
        if binary_search(custom, 0, len(store) - 1, store) != None:
            answer.append('yes')
        else:
            answer.append('no')

    return ' '.join(answer)

if __name__ == '__main__':
    TESTCASES = [
        [[5, 7, 9], [8, 3, 7, 9, 2]]
    ]
    for idx, (customer, store) in enumerate(TESTCASES):
        if solution(customer, store) == 'no yes yes':
            print(f'TESTCASE {idx+1} PASSED!')