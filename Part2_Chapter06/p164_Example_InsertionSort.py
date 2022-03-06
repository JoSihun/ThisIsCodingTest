def insert_sort(array):
    for idx in range(1, len(array)):
        for jdx in range(idx, 0, -1):
            if array[jdx] < array[jdx - 1]:
                array[jdx], array[jdx - 1] = array[jdx - 1], array[jdx]
            else:
                break
    return array

if __name__ == '__main__':
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    array = insert_sort(array)
    print(array)