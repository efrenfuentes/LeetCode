from solution import Solution

def test_original():
    solution = Solution()
    result = solution.lengthOfLongestSubstring("abcabcbb")
    assert result == 3


def test_same_character():
    solution = Solution()
    result = solution.lengthOfLongestSubstring("bbbbb")
    assert result == 1


def test_custom():
    solution = Solution()
    result = solution.lengthOfLongestSubstring("pwwkew")
    assert result == 3
