class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M = len(matrix)
        N = len(matrix[0])

        l = 0
        r = M * N - 1
        while l <= r:
            mid = (l + r) // 2
            x = mid // N
            y = mid % N
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False