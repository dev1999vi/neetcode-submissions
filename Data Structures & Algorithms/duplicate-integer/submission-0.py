class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = False
        new_set = set(nums)

        if(len(new_set) != len(nums)):
            res = True

        return res
        