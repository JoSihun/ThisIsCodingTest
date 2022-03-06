def select_sort(array):
    for idx in range(len(array)):
        min_idx = idx
        for jdx in range(idx + 1, len(array)):
            if array[jdx] < array[min_idx]:
                min_idx = jdx
        array[idx], array[min_idx] = array[min_idx], array[idx]
    return array

if __name__ == '__main__':
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    array = select_sort(array)
    print(array)