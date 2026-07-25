class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        i = 0
        j = m*n-1

        while i<=j:
            mid = i+(j-i)//2

            row, col = mid // m, mid%m

            if target > matrix[row][col]:
                i = mid + 1
            
            elif target < matrix[row][col]:
                j = mid-1

            else:
                return True
        return False