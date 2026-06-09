class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []

        for op in operations:
            print("result: ", result)
            print("op: ", op)

            if op == "C":
                result.pop()
                continue

            if op == "D":
                last_score = result.pop()
                result.append(last_score)
                result.append(last_score * 2)
                continue

            if op == "+":
                numbers = [result.pop(), result.pop()]

                result.append(numbers[1])
                result.append(numbers[0])
                result.append(sum(numbers))

                continue

            result.append(int(op))

        return sum(result)