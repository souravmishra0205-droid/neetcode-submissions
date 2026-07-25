class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixVal = 1
        postfixVal = 1
        output = [1]*len(nums)
        for i in range(1, len(nums)):
            output[i] = nums[i-1] * prefixVal
            prefixVal = output[i]
        
        for j in range(len(nums)-2, -1, -1):
            output[j] *= postfixVal * nums[j+1]
            postfixVal *= nums[j+1]
        
        return output

        
        