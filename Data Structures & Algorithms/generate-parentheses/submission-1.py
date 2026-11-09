class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        path = []

        def backtrack(open, closed):
            if len(path) == 2 * n:
                answer.append("".join(path))
                return

            if open < n:
                path.append("(")
                backtrack(open + 1, closed)
                path.pop()

            if closed < open:
                path.append(")")
                backtrack(open, closed + 1)
                path.pop()

        backtrack(0, 0)
        return answer
