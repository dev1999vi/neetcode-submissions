class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_stack = []
        result = [0] * len(temperatures)

        for i,temp in enumerate(temperatures):
            while temp_stack and temp > temp_stack[-1][0]:
                stack_temp, stack_index = temp_stack.pop()
                result[stack_index] = (i - stack_index)
            temp_stack.append([temp, i])

        return result