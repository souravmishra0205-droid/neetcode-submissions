class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = dict()
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        bucket = [[] for _ in range(len(nums) + 1)]

        for n, count in frequency.items():
            bucket[count].append(n) 
        
        ans = []

        for i in range(len(bucket)-1, 0, -1):
            for number in bucket[i]:
                ans.append(number)
                if len(ans) == k:
                    return ans
