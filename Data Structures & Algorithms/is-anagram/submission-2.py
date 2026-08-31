class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = {}
        t_freq = {}

        for c in s:
            if(c not in s_freq):
                s_freq[c] = 1
            else:
                s_freq[c] += 1

        for c in t:
            if(c not in t_freq):
                t_freq[c] = 1
            else:
                t_freq[c] += 1
        
        if len(s_freq) != len(t_freq):
            return False

        for key, value in s_freq.items():
            if((key not in t_freq) or t_freq[key] != value):
                return False

        return True