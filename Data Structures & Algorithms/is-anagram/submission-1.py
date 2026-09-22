class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freqS, freqT = {}, {}

        for l in s:
            if l in freqS:
                freqS[l] += 1
            else:
                freqS[l] = 1
        
        for l in t:
            if l in freqT:
                freqT[l] += 1
            else:
                freqT[l] = 1

        return freqS == freqT