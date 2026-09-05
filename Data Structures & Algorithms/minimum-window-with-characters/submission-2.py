class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        left = 0

        t_freq = {}

        for c in t:
            t_freq[c] = t_freq.get(c, 0) + 1

        win_freq = {}

        have = 0
        need = len(t_freq)

        minimum = float("inf")
        res = ""

        for right, char in enumerate(s):

            # Add character to window
            win_freq[char] = win_freq.get(char, 0) + 1

            # Character has now satisfied its required frequency
            if char in t_freq and win_freq[char] == t_freq[char]:
                have += 1

            # Window is valid
            while have == need:

                # Update minimum
                if right - left + 1 < minimum:
                    minimum = right - left + 1
                    res = s[left:right + 1]

                # Remove left character
                left_char = s[left]
                win_freq[left_char] -= 1

                # We just dropped below the required frequency
                if left_char in t_freq and win_freq[left_char] < t_freq[left_char]:
                    have -= 1

                if win_freq[left_char] == 0:
                    del win_freq[left_char]

                left += 1

        return res