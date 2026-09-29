class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for _, l in enumerate(s):
            if self.isOpeningBracket(l):
                stack.append(l)
            else:
                if not stack or not self.validClosingBracket(stack.pop(), l):
                    return False

        if not stack:
            return True
        return False
    
    def validClosingBracket(self, opening:str, closing: str) -> bool:
        return ((opening == '[' and closing == ']') or
        (opening == '(' and closing == ')') or
        (opening == '{' and closing == '}'))

    def isOpeningBracket(self, bracket:str) -> bool:
        return bracket == '[' or bracket == '(' or bracket == '{'