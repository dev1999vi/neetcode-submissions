class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        new_set = set()
        max_len = 0

        for i, char in enumerate(s):

            while char in new_set:
               new_set.remove(s[left])
               left += 1

            new_set.add(char)

            max_len = max(i - left + 1, max_len)

        return max_len