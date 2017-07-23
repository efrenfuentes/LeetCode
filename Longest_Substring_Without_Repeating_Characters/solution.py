class Solution(object):
    def start_without_repeat(self, s):
        result = ""
        for c in s:
            if c in result:
                return result
            else:
                result += c
        return result


    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        for idx, val in enumerate(s):
            my_string = self.start_without_repeat(s[idx:])
            if len(my_string) > max_len:
                max_len = len(my_string)
        return max_len
