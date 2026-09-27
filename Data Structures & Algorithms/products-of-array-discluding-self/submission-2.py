class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Solve without division: Build a prefix and suffix array for each index
        # prefix stores total product left of arry and siffix stores to left of each index
        # end is to multiply the prefix with suffix for result
        n = len(nums)
        prefix, suffix = [0] * n, [0] * n
        prefix[0] = suffix[n-1] = 1
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        res = [0] * n
        for i in range(n):
            res[i] = suffix[i] * prefix[i]

        return res