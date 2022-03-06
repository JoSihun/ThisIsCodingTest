def counting_sort(array):
    count = [0] * (max(array) + 1)

    for idx in range(len(array)):
        count[array[idx]] += 1

    answer = []
    for idx in range(len(count)):
        for jdx in range(count[idx]):
            answer.append(idx)

    return answer

if __name__ == '__main__':
    array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
    array = counting_sort(array)
    print(array)