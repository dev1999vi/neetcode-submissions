class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i,num in enumerate(nums):
            difference = target - num
            # Check if the complement already exists in our map
            if difference in nums_dict:
                return [nums_dict[difference], i]
            
            # If not, store the current number and its index
            nums_dict[num] = i

        return [-1,-1]

