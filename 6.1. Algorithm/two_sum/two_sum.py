def two_sum(nums, target):
    seen = {}
    for idx, value in enumerate(nums):
        compl = target - value
        if compl in seen:
            return [seen[compl], idx]
        seen[value] = idx
    return []

arr = [2, 7, 11, 15]
target = 9
print(two_sum(arr, target))