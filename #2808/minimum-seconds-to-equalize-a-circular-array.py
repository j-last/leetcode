from math import inf

def minimumSeconds(nums: list[int]) -> int:
    seconds = inf
    for num in set(nums):
        if nums.count(num) < len(nums) / (3 * seconds):
            continue
        indexes = [index for index in range(len(nums)) if nums[index] == num]
        # Find the largest gap between any two of this number,
        # starting with the last occurence -> first occurence gap
        biggest_gap = len(nums) - indexes[-1] + indexes[0] - 2
        for index in range(len(indexes) - 1):
            biggest_gap = max(biggest_gap, indexes[index + 1] - indexes[index] - 1)
        
        seconds = min(seconds, (biggest_gap + 1) // 2)
    return seconds
