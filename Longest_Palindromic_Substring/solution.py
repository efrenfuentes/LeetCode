class Solution(object):
    def is_palindrome(self, s):
        b = list(s)
        b.reverse()
        s2 = ''.join(b)

        if s == s2:
            return True
        else:
            return False


    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if (len(s) == 1) or (self.is_palindrome(s)):
            return s

        max_palindrome = ""
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                my_string = s[i:j]
                if self.is_palindrome(my_string):
                    if len(my_string) > len(max_palindrome):
                        max_palindrome = my_string

        return max_palindrome
