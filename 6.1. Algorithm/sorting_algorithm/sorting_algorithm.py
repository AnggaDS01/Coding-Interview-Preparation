def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # print(f"key {key}, arr = {arr[j]}")
        while j >= 0 and key <= arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print(insertion_sort(arr))
