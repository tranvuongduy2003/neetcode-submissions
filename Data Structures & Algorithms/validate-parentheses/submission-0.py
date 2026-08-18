class Solution:
    def isValid(self, s: str) -> bool:
        m = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        stack = []
        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            else:
                if not bool(stack):
                    return False
                closed = stack.pop()
                if m[closed] != c:
                    return False

        if not bool(stack):
            return True
        return False