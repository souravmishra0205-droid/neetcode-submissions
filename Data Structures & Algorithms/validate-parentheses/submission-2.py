class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {"}": "{", ")":"(", "]":"["}
        for ele in s:
            if ele in ["(", "{", "["]:
                stack.append(ele)

            else:
                if ele in [")", "}", "]"]:
                    if stack:
                        item = stack.pop()
                        if item!=lookup[ele]:
                            return False
                    else:
                        stack.append(ele)
        return True if not stack else False
