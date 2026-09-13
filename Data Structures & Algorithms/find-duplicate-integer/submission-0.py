class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            num = abs(num)
            if nums[num] > 0:
                # not visited
                nums[num] = - nums[num]
            else:
                return num