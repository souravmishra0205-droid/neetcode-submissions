class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookupNums = set(nums)
        maxi = 0
        for num in lookupNums:
            count = 1
            if num-1 in lookupNums:
                continue
            else:
                while num+1 in lookupNums:
                    count += 1
                    num+=1
                maxi = max(maxi, count)
        return maxi


        