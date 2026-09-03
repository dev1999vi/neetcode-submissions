class Solution:
    # def invalid_freq(freq, k):
    #     return 

    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freq = {}
        max_len = 0
        max_freq = 0

        for i, char in enumerate(s):
            freq[char] = freq.get(char, 0) + 1
            max_freq = max(max_freq, freq[char])
            while (i - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del(freq[s[left]])
                left += 1

            max_len = max(max_len, i - left + 1)

        return max_len
            