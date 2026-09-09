class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        max_product = 1
        zero_count = 0
        for val in nums:
            if val == 0:
                zero_count += 1
            if zero_count > 1:
                return [0] * len(nums)
            elif zero_count == 1 :
                if val == 0: 
                    continue
                max_product *= val
            else:
                max_product *= val
        if zero_count == 1:
            print(max_product)
        res = []

        for val in nums:
            if zero_count == 1 and val == 0:
                res.append(max_product)
            elif zero_count == 1 and val != 0:
                res.append(0)
            else:
                res.append(int(max_product/val))

        return res 