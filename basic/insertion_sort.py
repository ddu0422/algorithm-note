# 오름차순
def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            else:
                break

    return array


# 내림차순
def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] > array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            else:
                break

    return array
