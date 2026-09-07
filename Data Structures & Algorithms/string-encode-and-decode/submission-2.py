class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_chunks = []
        for s in strs:
            encoded_chunks.append(f"{len(s)}#{s}")
        return "".join(encoded_chunks)


    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []

        res = []
        print(s)
        i = 0
        while(i < len(s)):
            left = i+2
            right = s[i]
            while(s[i+1] != '#'):
                left += 1
                right += s[i+1]
                i +=1
            res.append(s[left:(left+int(right))])
            i = i + (int(right) + 2)

        return res
