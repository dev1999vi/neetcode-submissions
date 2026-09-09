class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_set = set(nums)
        longest = 0

        for n in new_set:
            if n-1 not in new_set:
                length = 1
                while length + n in new_set:
                    length += 1
                longest = max(length, longest)

        return longest