class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list) # [1, 1, ... , 1] -> ["abs", "bas"]

        for i, word in enumerate(strs):
            freqArray = [0] * 26
            for j, letter in enumerate(word):
                freqArray[ord(letter) - 97] +=1
        
            groups[tuple(freqArray)].append(word)

        return list(groups.values())