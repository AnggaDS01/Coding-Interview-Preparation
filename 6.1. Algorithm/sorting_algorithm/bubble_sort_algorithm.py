def bubble_sort(arr):  # (1)
    for i in range(len(arr)):  # (2)
        for j in range(len(arr) - 1):  # (3)
            if arr[j] > arr[j + 1]:  # (4)
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # (5)
    return arr  # (6)

arr = [64, 34, 25, 12, 22, 11, 90, 1]  # (7)
print(bubble_sort(arr))  # (8)
