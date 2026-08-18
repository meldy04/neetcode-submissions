class Solution:
    def calPoints(self, operations: List[str]) -> int:
        acc = []
        for op in operations:
            if op == "+":
                acc.append(acc[-1] + acc[-2])
            elif op == "D":
                acc.append(acc[-1] * 2)
            elif op == "C":
                acc.pop()
            else:
                acc.append(int(op))
        return sum(acc)