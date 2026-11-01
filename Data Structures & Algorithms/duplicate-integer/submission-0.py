class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsMap = {}
        for num in nums:
            if not num in numsMap:
                numsMap[num] = 1
            else:
                return True
        return False

        