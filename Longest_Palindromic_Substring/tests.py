from solution import Solution

def test_original():
    solution = Solution()
    result = solution.longestPalindrome("babad")
    assert (result == "bab") or (result == "aba")


def test_custom():
    solution = Solution()
    result = solution.longestPalindrome("cbbd")
    assert result == "bb"


def test_on_character():
    solution = Solution()
    result = solution.longestPalindrome("c")
    assert result == "c"


def test_two_character():
    solution = Solution()
    result = solution.longestPalindrome("bb")
    assert result == "bb"


def test_on_end():
    solution = Solution()
    result = solution.longestPalindrome("abb")
    assert result == "bb"
