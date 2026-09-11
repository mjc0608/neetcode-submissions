class Solution:
    def findMin(self, nums: List[int]) -> int:
        N = len(nums)

        l = 0
        r = N - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            else:
                if nums[mid] > nums[r]:
                    l = mid + 1
                elif nums[mid] < nums[l]:
                    r = mid - 1
                else:
                    # this is ordered
                    return nums[l]

        return nums[mid]
                    
