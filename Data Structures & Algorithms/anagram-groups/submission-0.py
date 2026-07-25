from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictList = defaultdict(list)
        for string in strs:
            lookupList = [0]*26
            for char in string:
                lookupList[ord(char) - ord('a')] += 1
            
            dictList[tuple(lookupList)].append(string)
        
        return list(dictList.values())
        