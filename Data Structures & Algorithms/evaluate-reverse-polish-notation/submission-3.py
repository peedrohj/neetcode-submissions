"""

Create an algorithm that can calculate an arithmetic experssion using
the reverse polish notation
Input: tokens = ["1","2","+","3","*","4","-"]
Output: 5

Requirements:
- The operands may be integers or the results of other operations.
- The operators include '+', '-', '*', and '/'.
- Assume that division between integers always truncates toward zero
- tokens[i] is "+", "-", "*", or "/", or a string representing an
  integer in the range [-200, 200].
- The polish notation is when the operator appears after the operands (1,2,+)
  instead of (1,+,2)

Solution:
- Use a stack to add all valid numbers.
- When identify a operator remove all values from queue
  and store the result in the same queue


"""


class Solution:
    def calculate(self, num1: int, num2: int, token: str) -> int:

        operations = {
            "+": lambda x, y: x + y,
            "*": lambda x, y: x * y,
            "-": lambda x, y: x - y,
            "/": lambda x, y: x / y,
        }

        return int(operations[token](num1, num2))

    def evalRPN(self, tokens: List[str]) -> int:
        queue = collections.deque()

        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                num2 = queue.pop()
                num1 = queue.pop()

                result = self.calculate(num1=num1, num2=num2, token=token)
                queue.append(result)
                
                continue


            queue.append(int(token))

        result = queue.pop()

        return result
