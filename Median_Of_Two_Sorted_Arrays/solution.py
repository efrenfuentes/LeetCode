class Solution:
    def median(self, mylist):
        sorts = sorted(mylist)
        length = len(sorts)
        if not length % 2:
            return (sorts[int(length / 2)] + sorts[int(length / 2 - 1)]) / 2.0
        return sorts[int(length / 2)]

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2

        return self.median(nums)
