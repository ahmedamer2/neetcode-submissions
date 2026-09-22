class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}

        for i, n in enumerate(nums):
            res = target-n
            if n in diff:
                return [diff[n], i]
            diff[res] = i
        