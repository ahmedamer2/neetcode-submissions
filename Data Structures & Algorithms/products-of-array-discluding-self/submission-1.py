class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Simple solution: loop through and multiply all digits
        # Loop through solution array and add in total / num[i]
        # if 1 zero then all zero except for index where num[i] = 0
        # if more than 1 zero then all zeros

        total = 1
        zeroCount = 0
        for num in nums:
            if num == 0:
                zeroCount += 1
            else:
                total *= num

        if zeroCount > 1:
            return [0] * len(nums)
        
        res = [0] * len(nums)

        for i, num in enumerate(nums):
            if zeroCount > 0:
                if num == 0:
                    res[i] = total
                else:
                    res[i] = 0
            else:
                res[i] = total//num

        return res