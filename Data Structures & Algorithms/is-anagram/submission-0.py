class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = {}
        hash2 = {}
        for i in s:
            if not i in hash1:
                hash1[i] = 1
            else:  
                hash1[i] += 1
        
        for j in t:
            if not j in hash2:
                hash2[j] = 1
            else:
                hash2[j] += 1

        return (hash1 == hash2)