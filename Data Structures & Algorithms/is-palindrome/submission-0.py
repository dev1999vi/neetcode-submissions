class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = re.findall(r'\w', s)
        i = 0
        j = len(result) - 1

        res = True

        while(i<j):
            if(result[i].lower() != result[j].lower()):
                res = False
                break
            
            i += 1
            j -= 1


        return res
