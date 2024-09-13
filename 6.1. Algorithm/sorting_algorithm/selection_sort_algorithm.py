def selection_sort(arr):
    for i in range(len(arr)):  # (1)
        min_idx = i  # (2)
        for j in range(i + 1, len(arr)):  # (3)
            if arr[j] < arr[min_idx]:  # (4)
                min_idx = j  # (5)
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # (6)
    return arr  # (7)

arr = [64, 34, 25, 12, 22, 11, 90, 1]  # (8)
print(selection_sort(arr))  # (9)