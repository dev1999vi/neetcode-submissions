class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        left = 0
        s1_freq = [0] * 26
        for s in s1:
            s1_freq[ord(s) - ord('a')] +=1
        s2_freq = [0] * 26
        res = False
        win_len = len(s1)

        for i,char in enumerate(s2):
            s2_freq[ord(char) - ord('a')] +=1

            if i - left + 1 > win_len:
                s2_freq[ord(s2[left]) - ord('a')] -= 1
                left +=1
            
            if s1_freq == s2_freq:
                return True

        return res