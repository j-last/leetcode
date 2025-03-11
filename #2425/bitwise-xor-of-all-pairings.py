"""
Did the boolean algebra to find that if the other list had an even
number of elements, the numbers in the current list would end up being
XOR'd with themselves an even number of times, resulting in 0.

Hence, XOR-ing all numbers in the odd-length lists gets the solution.
"""
def xorAllNums(nums1: list[int], nums2: list[int]) -> int:
    final_num = 0
    if len(nums1) % 2 == 1:
        for num in nums1:
            final_num ^= num
    if len(nums2) % 2 == 1:
        for num in nums2:
            final_num ^= num
    return final_num
