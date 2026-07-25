class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = dict()
        lookup[nums[0]]=0

        for i in range(1, len(nums)):
            diff = target - nums[i]
            if diff in lookup:
                return [lookup[diff],i]
            else:
                lookup[nums[i]]=i
