class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #  i  j       k=0
        # AAABAABBBBBB
        # window - freq of most freq char <= k then window is valid

        freq = {}
        l, res = 0, 0

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            if (r - l + 1) - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res

        