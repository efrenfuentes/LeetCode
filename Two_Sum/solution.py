class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for idx, value in enumerate(nums):
            complement = target - value
            try:
                found = nums.index(complement)
                if idx != found:
                    return [idx, found]
            except ValueError:
                continue

        return []
