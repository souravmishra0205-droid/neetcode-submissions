class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i = 0
        j = 0
        m = len(s1)
        n = len(s2)

        mapS1 = {}
        mapS2 = {}

        for k in range(m):
            mapS1[s1[k]] = mapS1.get(s1[k], 0) + 1
        
        lenMapS1 = len(mapS1)

        while j<n:
            mapS2[s2[j]] = mapS2.get(s2[j], 0) + 1

            if j-i+1 < m:
                j+=1

            else:
                if mapS1 == mapS2:
                    return True
                
                mapS2[s2[i]] -= 1
                if mapS2[s2[i]] == 0:
                    del mapS2[s2[i]]
                    
                i+=1
                j+=1
        return mapS1 == mapS2


