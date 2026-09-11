class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        while l + 1 < r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid
            else:
                l = mid
        
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        else:
            return -1