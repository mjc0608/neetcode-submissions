class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in {'+', '-', '*', '/'}:
                stack.append(int(token))
            else:
                a = stack[-2]
                b = stack[-1]
                stack.pop()
                stack.pop()
                if token == '+':
                    r = a + b
                elif token == '-':
                    r = a - b
                elif token == '*':
                    r = a * b
                else:
                    r = int(a / b)
                stack.append(r)
        return stack[0]