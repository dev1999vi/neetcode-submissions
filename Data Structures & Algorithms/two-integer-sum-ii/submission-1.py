class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right = len(numbers) - 1
        for i, val in enumerate(numbers):
            sum = val + numbers[right]
            while(sum > target):
                right -= 1
                sum = val + numbers[right]
            
            if sum == target:
                return[i+1, right + 1]


        return []