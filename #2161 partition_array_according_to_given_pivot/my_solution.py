class Solution:
    def pivotArray(self, nums, pivot):
        """Rearranges the nums list so that elements are arranged into
        3 sections: less than pivot, equal to pivot and greater than
        pivot. The relative order of elements in these sections must be
        maintained.

        Args:
            nums (list[int]): The list of numbers to rearrange.
            pivot (int): The value of the pivot.

        Returns:
            list[int]: The rearranged list of numbers.
        """
        less_than, equal_to, greater_than = [], [], []
        for num in nums:
            if num < pivot:
                less_than.append(num)
            elif num > pivot:
                greater_than.append(num)
            else:
                equal_to.append(num)
        return less_than + equal_to + greater_than
