class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashed = {}
        for i in range(len(nums)):
            if target-nums[i] in hashed:
                return [hashed[target-nums[i]], i]
            if not nums[i] in hashed:
                hashed[nums[i]] = i
            

        

