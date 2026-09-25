class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #num -> freq

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        # Create bucket array where freq = index and elements is array of index freq elements
        freq = [[] for _ in range(len(nums)+1)]

        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        

        