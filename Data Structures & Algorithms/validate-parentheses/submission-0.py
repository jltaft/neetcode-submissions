class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p = {')':'(', '}': '{', ']': '['}
        for i in s:
            if i in p.values():
                stack.append(i)
            if i in p.keys():
                if len(stack) != 0 and stack[-1] == p[i]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False