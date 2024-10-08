def two_sum(nums, target):  # (1)
    seen = {}  # (2)
    for idx, value in enumerate(nums):  # (3)
        compl = target - value  # (4)
        if compl in seen:  # (5)
            return [seen[compl], idx]  # (6)
        seen[value] = idx  # (7)
    return []  # (8)

arr = [2, 7, 11, 15]  # (9)
target = 9  # (10)
print(two_sum(arr, target))  # (11)