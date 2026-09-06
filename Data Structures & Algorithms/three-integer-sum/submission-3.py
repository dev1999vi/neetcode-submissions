class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, val in enumerate(nums):
            target = -val
            j = i+1
            k = len(nums) - 1

            while(j<k):
                sum = nums[j] + nums[k]
                if sum > target:
                    k -= 1
                elif target > sum:
                    j += 1
                elif sum == target:
                    if [val,nums[j], nums[k]] not in res:
                        res.append([val,nums[j], nums[k]])
                    j += 1
                    k -= 1

        return res