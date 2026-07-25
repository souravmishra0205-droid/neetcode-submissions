class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        n = len(s)
        
        longest = 0
        myDict = {}
        while j<n:
            myDict[s[j]] = myDict.get(s[j], 0) + 1

            if j-i+1 == len(myDict):
                longest = max(longest, j-i+1)
                j+=1
            
            else:
                while j-i+1 > len(myDict):
                    myDict[s[i]] -= 1
                    if myDict[s[i]] == 0:
                        del myDict[s[i]]
                    i+=1
                j+=1
        return longest

