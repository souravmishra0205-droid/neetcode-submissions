
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        i = 0
        j = 0
        maxi = 0
        counter = {}
        res = 0
        while j <n:
            counter[s[j]] = counter.get(s[j], 0) + 1
            maxi = max(maxi, counter[s[j]])

            if j-i+1 - maxi <= k:
                pass

            else:
                while (j-i+1) - maxi > k:
                    counter[s[i]] -= 1
                    if counter[s[i]] == 0:
                        del counter[s[i]]
                    i+=1
                
            res = max(res, j-i+1)
            j+=1
        return res
