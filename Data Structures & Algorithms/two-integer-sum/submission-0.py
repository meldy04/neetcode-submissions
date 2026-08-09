class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in values:
                return [values[difference], i]
            values[num] = i