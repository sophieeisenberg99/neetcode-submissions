class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        seen = [False] * len(nums)

        def backtrack():
            if len(path) == len(nums):
                result.append(path.copy())
                return

            for i in range(len(nums)):
                if not seen[i]:
                    path.append(nums[i])
                    seen[i] = True

                    backtrack()

                    path.pop()
                    seen[i] = False

        backtrack()
        return result
        