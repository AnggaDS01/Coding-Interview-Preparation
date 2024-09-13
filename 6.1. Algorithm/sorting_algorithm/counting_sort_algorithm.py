def counting_sort(arr):
    if arr:
        max_val = max(arr)
        count = [0] * (max_val + 1)
        output = [0] * len(arr)

        for num in arr:
            count[num] += 1

        for i in range(1, len(count)):
            count[i] += count[i - 1]

        for num in reversed(arr):
            output[count[num] - 1] = num
            count[num] -= 1

        return output

    return arr

arr = [64, 34, 25, 12, 22, 11, 90, 1]
print(counting_sort(arr))