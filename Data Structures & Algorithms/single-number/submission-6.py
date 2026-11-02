class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        ind = 0
        while ind + 1 < len(nums):
            if nums[ind] != nums[ind + 1]:
                return nums[ind]
            ind += 2
        return nums[-1]