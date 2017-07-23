from solution import Solution

def test_original():
    solution = Solution()
    result = solution.findMedianSortedArrays([1, 3], [2])
    assert result == 2.0

def test_custom():
    solution = Solution()
    result = solution.findMedianSortedArrays([1, 2], [3, 4])
    assert result == 2.5
