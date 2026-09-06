class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_cap = 0
        i = 0
        j = len(heights) - 1
        print(f"len {j}")

        while(i < j):
            curr_cap = (j-i) * min(heights[i], heights[j])
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
            
            max_cap = max(max_cap, curr_cap)

        return max_cap