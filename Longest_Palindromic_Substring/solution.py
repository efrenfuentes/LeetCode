class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        length = len(s)

        if (length == 1) or (s == s[::-1]):
            return s

        max_palindrome = s[0]
        i = 1
        while (i < length) and (s[i] == s[0]):
            max_palindrome = s[0:i]
            i += 1

        length_palindrome = 1
        i = 0
        while i < length:
            j = i + length_palindrome
            while j < length + 1:
                my_string = s[i:j]
                if my_string == my_string[::-1]:
                    if len(my_string) > length_palindrome:
                        max_palindrome = my_string
                        length_palindrome = len(max_palindrome)
                j += 1
            i += 1

        return max_palindrome
