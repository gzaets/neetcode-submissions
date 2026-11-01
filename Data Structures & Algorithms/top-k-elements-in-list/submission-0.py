class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashed = {}
        frequency = [[] for i in range(len(nums)+1)]
        for num in nums:
            if not num in hashed:
                hashed[num] = 1
            else:
                hashed[num] += 1

        for key, count in hashed.items():
            frequency[count].append(key)
        
        res = []
        for i in range(len(frequency)-1, -1, -1):
            for n in frequency[i]:
                res.append(n)
                k-=1
                if k == 0:
                    return res
