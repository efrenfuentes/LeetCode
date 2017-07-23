# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution(object):

    @staticmethod
    def linked_to_list(linked, list=None):
        if list is None:
            list = []

        list.insert(len(list), linked.val)
        if linked.next is None:
            return list
        else:
            return Solution.linked_to_list(linked.next, list)

    @staticmethod
    def list_to_linked(list):
        if len(list) == 0:
            return None
        else:
            list_node = ListNode(list[0])
            list_node.next = Solution.list_to_linked(list[1:])
            return list_node


    @staticmethod
    def number_to_linked(number):
        if number == 0:
            list = [0]
        else:
            list = []
        
        while number > 0:
            number, residue = divmod(number, 10)
            list.insert(len(list), residue)
        return Solution.list_to_linked(list)


    @staticmethod
    def linked_to_number(linked):
        list = Solution.linked_to_list(linked)
        number = 0
        for idx, value in enumerate(list):
            number = number + value * 10**idx

        return number


    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        sum = Solution.linked_to_number(l1) + Solution.linked_to_number(l2)

        return Solution.number_to_linked(sum)
