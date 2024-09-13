'''
Merge Sort membagi array menjadi sub-array kecil, kemudian menggabungkannya kembali dengan urutan yang benar.
'''

def merge_sort(arr):
    if len(arr) > 1:  # (1)
        mid = len(arr) // 2  # (2)
        left_half = arr[:mid]  # (3)
        right_half = arr[mid:]  # (4)

        merge_sort(left_half)  # (5)
        merge_sort(right_half)  # (6)

        i = j = k = 0  # (7)
        while i < len(left_half) and j < len(right_half):  # (8)
            if left_half[i] < right_half[j]:  # (9)
                arr[k] = left_half[i]  # (10)
                i += 1  # (11)
            else:
                arr[k] = right_half[j]  # (12)
                j += 1  # (13)
            k += 1  # (14)

        while i < len(left_half):  # (15)
            arr[k] = left_half[i]  # (16)
            i += 1  # (17)
            k += 1  # (18)

        while j < len(right_half):  # (19)
            arr[k] = right_half[j]  # (20)
            j += 1  # (21)
            k += 1  # (22)
    return arr  # (23)

arr = [64, 34, 25, 12, 22, 11, 90, 1]  # (24)
print(merge_sort(arr))  # (25)
