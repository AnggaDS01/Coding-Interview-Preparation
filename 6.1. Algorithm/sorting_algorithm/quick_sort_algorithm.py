def quick_sort(arr):  # (1)
    if len(arr) <= 1:  # (2)
        return arr  # (3)

    pivot = arr[len(arr) // 2]  # (4)
    left = [x for x in arr if x < pivot]  # (5)
    middle = [x for x in arr if x == pivot]  # (6)
    right = [x for x in arr if x > pivot]  # (7)
    
    return quick_sort(left) + middle + quick_sort(right)  # (8)

arr = [64, 34, 25, 12, 22, 11, 90, 1]  # (9)
print(quick_sort(arr))  # (10)