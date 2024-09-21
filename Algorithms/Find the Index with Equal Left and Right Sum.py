def equivalent_index(nums):
    total_sum = sum(nums)
    left_sum = 0

    for i in range(len(nums)):
        left_sum += nums[i] 
        if left_sum == total_sum - left_sum-nums[i]:
            return i
    return -1
