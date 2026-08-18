class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            match t:
                case '+':
                    x = stack.pop()
                    y = stack.pop()
                    stack.append(y + x)
                case '-':
                    x = stack.pop()
                    y = stack.pop()
                    stack.append(y - x)
                case '*':
                    x = stack.pop()
                    y = stack.pop()
                    stack.append(y * x)
                case '/':
                    x = stack.pop()
                    y = stack.pop()
                    stack.append(math.trunc(y / x))
                case _:
                    stack.append(int(t))
        return stack.pop()

