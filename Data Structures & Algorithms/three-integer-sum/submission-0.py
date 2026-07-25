class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        output = set()
        ans = []

        n = len(nums)

        i = 0
        j = n-1

        for i in range(n):
            j = i+1
            k = n-1
            sumNums = []
            while j<k:

                sumNums =  nums[i] + nums[j] + nums[k]

                if sumNums == 0:
                    output.add(tuple([nums[i],nums[j],nums[k]]))
                    j+=1
                    k-=1

                elif sumNums > 0:
                    k -= 1
                else: 
                    j+=1

        for ele in output:
            ans.append(list(ele))
        return ans


        