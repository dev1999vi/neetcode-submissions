class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        for char in s:
            if char == ']' or char == ')' or char == '}':
                if len(stack) > 0 and self.is_valid(char, stack[-1]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
            
             
        if not stack:
            return True
        else:
            return False

    def is_valid(self, char: str, top: str) -> bool:
        if char == ']' and top == '[':
            return True
        elif char == ')' and top == '(':
            return True
        elif char == '}' and top == '{':
            return True
        else:
            return False