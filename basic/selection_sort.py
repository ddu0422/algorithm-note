# 오름차순
def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

    return array


# 내림차순
def selection_sort(array):
    for i in range(len(array)):
        max_index = i
        for j in range(i, len(array)):
            if array[max_index] < array[j]:
                max_index = j
        array[i], array[max_index] = array[max_index], array[i]

    return array
