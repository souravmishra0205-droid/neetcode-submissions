class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # TC: O(N*M), SC: O(N)
        # searchArr = []

        # n = len(matrix)
        # m = len(matrix[0])

        # for i in range(n):
        #     searchArr.extend(matrix[i])

        # i = 0
        # j = len(searchArr)-1

        # while i<=j:
        #     mid = i+ (j-i)//2

        #     if searchArr[mid] == target:
        #         return True

        #     elif searchArr[mid] > target:
        #         j = mid - 1
        #     else:
        #         i = mid + 1

        # return False

        n = len(matrix)  # row
        m = len(matrix[0]) # col

        i = 0
        j = n*m-1

        while i<=j:
            mid = i + (j-i)//2

            row = mid//m
            col = mid%m

            if matrix[row][col] == target:
                return True

            elif matrix[row][col] > target:
                j = mid - 1

            else:
                i = mid + 1
        return False