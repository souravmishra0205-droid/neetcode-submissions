class Solution:
    def trap(self, height: List[int]) -> int:
        # TC: O(n^2), SC: O(1)
        # storage = 0
        # for i in range(1, len(height)-1):
        #     prevMax = max(height[:i])
        #     nextMax = max(height[i+1:])
        #     log = min(prevMax, nextMax) - height[i]
        #     if log>0:
        #         storage+=log
        # return storage

        # TC: O(N), SC: O(N)
        # n = len(height)
        # prevmaxArr = [0]*n
        # nextmaxArr = [0]*n
        # storage = 0

        # for i in range(1, n):
        #     prevmaxArr[i] = max(prevmaxArr[i-1], height[i-1])

        # for j in range(n-2, -1, -1):
        #     nextmaxArr[j] = max(nextmaxArr[j+1], height[j+1])
        
        # for k in range(n):
        #     log = min(nextmaxArr[k], prevmaxArr[k]) - height[k]
        #     if log>0:
        #         storage+=log
        # return storage

        n = len(height)
        i = 0
        j = n-1
        storage = 0
        prevMax = height[0]
        nextMax = height[n-1]

        while i<j:
            if prevMax < nextMax:
                i += 1
                prevMax = max(prevMax, height[i])
                storage += prevMax - height[i]

            else:
                j-=1
                nextMax = max(nextMax, height[j])
                storage += nextMax - height[j]
        return storage



        