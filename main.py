def find_max(nums):
    max_num = nums[0]
    for n in nums:
        if n > max_num:
            max_num = n
    return max_num

print(find_max([3, 8, 2, 10, 5]))
