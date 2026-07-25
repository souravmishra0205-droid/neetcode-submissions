class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookupTable = dict()

        for i, num in enumerate(nums):
            diff = target - num
            if diff in lookupTable:
                return [lookupTable[diff], i]
            else:
                lookupTable[num] = i
        return -1
        