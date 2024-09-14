def insertion_sort(arr):
    for i in range(1, len(arr)):  # (1)
        key = arr[i]  # (2)
        j = i - 1  # (3)
        while j >= 0 and key < arr[j]:  # (4)
            arr[j + 1] = arr[j]  # (5)
            j -= 1  # (6)
        arr[j+1] = key  # (7)
    return arr  # (8)

arr = [64, 34, 25, 12, 22, 11, 90, 1]  # (9)
print(insertion_sort(arr))  # (10)