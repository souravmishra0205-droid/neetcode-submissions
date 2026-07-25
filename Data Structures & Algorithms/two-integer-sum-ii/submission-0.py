class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i = 0
        j = n-1

        while i<j:

            sumval = numbers[i] + numbers[j]
            if sumval < target:
                i+=1
            elif sumval > target:
                j-=1
            else:
                return [i+1, j+1]
        
        return [-1, -1]
        