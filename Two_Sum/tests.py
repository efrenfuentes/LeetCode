from solution import Solution

def test_original():
    solution = Solution()
    result = solution.twoSum([2, 7, 11, 15], 9)
    assert result == [0, 1]

def test_custom():
    solution = Solution()
    result = solution.twoSum([3,2,4], 6)
    assert result == [1,2]
