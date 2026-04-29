class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        operations = [ '+', '-', '*', '/']

        for i in range(len(tokens)):
            if tokens[i] in operations:
                a = stack.pop()
                b = stack.pop()

                match tokens[i]:
                    case '+':
                        stack.append(b + a) 
                    case '-':
                        stack.append(b - a) 
                    case '*':
                        stack.append(a * b) 
                    case '/':
                        stack.append(int(b / a))
            else:
                stack.append(int(tokens[i]))
        
        return stack.pop()