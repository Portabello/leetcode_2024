class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closed_bracket = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if c in [')', ']', '}']:
                    if stack[-1] == closed_bracket[c]:
                        stack.pop()
                    else:
                        return False
        if len(stack) == 0:
            return True
        return False
