class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): return False

        dictS = dict()
        dictT = dict()

        for stringS, stringT in zip(s,t):
            dictS[stringS] = dictS.get(stringS, 0) + 1
            dictT[stringT] = dictT.get(stringT, 0) + 1
        
        return dictS == dictT
