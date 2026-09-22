class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        target_arr = None

        low  = 0
        high = len(matrix) - 1

        while low <= high:
            mid = (low + high) // 2
            print(mid)
            if(matrix[mid][0] <= target and matrix[mid][-1] >= target):
                target_arr = matrix[mid]
                break
            elif(matrix[mid][0] > target):
                high = mid - 1
            else:
                low = mid + 1

        if target_arr == None:
            return False
            
        low = 0
        high = len(target_arr) - 1

        while low <= high:
            mid = (low + high) // 2

            if(target_arr[mid] == target):
                return True
            elif(target_arr[mid] > target):
                high = mid - 1
            else:
                low = mid + 1

        return False
