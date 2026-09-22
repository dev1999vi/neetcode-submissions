class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == 1:
            return math.ceil(piles[0]/h)
        upper = max(piles)
        result = upper

        l = 1
        high = upper

        while l <= high:
            hour = 0
            mid  = (l+high) // 2

            for pile in piles:
                hour += math.ceil(pile/mid)
            
            if h >= hour:
                result = min(result, mid)
                high = mid - 1
            else:
                l = mid + 1
            
        return result