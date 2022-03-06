def quick_sort1(start, end, array):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort1(start, right - 1, array)
    quick_sort1(right + 1, end, array)
    return array

def quick_sort2(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]
    return quick_sort2(left) + [pivot] + quick_sort2(right)

if __name__ == '__main__':
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    array1 = quick_sort1(0, len(array) - 1, array)
    array2 = quick_sort2(array)
    print(array1)
    print(array2)