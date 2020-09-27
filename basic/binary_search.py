# 재귀
def binary_serach(array, target, start, end):
    if start > end:
        return

    mid = (start + end) // 2

    if target == array[mid]:
        return mid
    elif target < array[mid]:
        return binary_serach(array, target, start, mid - 1)
    else:
        return binary_serach(array, target, start, mid + 1)


# 반복문
def binary_serach(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if target == array[mid]:
            return mid
        elif target < array[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return
