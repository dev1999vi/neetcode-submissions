class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        freq = {}
        max = 0

        for i, char in enumerate(s):
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1

            while freq[char] > 1:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1

            current_len = i - left + 1

            if current_len > max:
                max = current_len

        return max