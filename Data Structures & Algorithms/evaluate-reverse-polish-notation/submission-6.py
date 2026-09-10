class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        # Using a set for O(1) lookups
        operators = {'+', '-', '*', '/'}

        for t in tokens:
            # Check if the token is an operator
            if t in operators:
                # The first pop is the second operand (op2)
                # The second pop is the first operand (op1)
                op2 = stack.pop()
                op1 = stack.pop()
                
                # Perform the operation and push the integer result
                if t == '+':
                    stack.append(op1 + op2)
                elif t == '-':
                    stack.append(op1 - op2)
                elif t == '*':
                    stack.append(op1 * op2)
                elif t == '/':
                    # In Python, int(op1 / op2) correctly truncates toward zero
                    stack.append(int(op1 / op2))
            else:
                # Convert numbers to integers immediately before pushing
                stack.append(int(t))

        return stack[-1]