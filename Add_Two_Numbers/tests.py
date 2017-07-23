from solution import Solution


def test_original():
    l1 = Solution.number_to_linked(342)
    l2 = Solution.number_to_linked(465)
    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    assert Solution.linked_to_list(result) == [7, 0, 8]
    assert Solution.linked_to_number(result) == 807


def test_custom():
    l1 = Solution.number_to_linked(564)
    l2 = Solution.number_to_linked(743)
    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    assert Solution.linked_to_list(result) == [7, 0, 3, 1]
    assert Solution.linked_to_number(result) == 1307


def test_zero():
    l1 = Solution.number_to_linked(0)
    l2 = Solution.number_to_linked(0)
    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    assert Solution.linked_to_list(result) == [0]
    assert Solution.linked_to_number(result) == 0
