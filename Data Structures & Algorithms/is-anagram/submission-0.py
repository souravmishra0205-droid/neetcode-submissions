class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = dict()
        dictT = dict()

        for ele in s:
            dictS[ele] = dictS.get(ele, 0) + 1

        for ele2 in t:
            dictT[ele2] = dictT.get(ele2, 0) + 1

        return dictS == dictT
        