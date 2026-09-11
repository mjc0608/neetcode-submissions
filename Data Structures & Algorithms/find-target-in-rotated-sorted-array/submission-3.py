class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)

        l = 0
        r = N - 1

        base_idx = None
        base_val = None
        while l <= r:
            mid = (l + r) // 2
            if nums[mid-1] > nums[mid]:
                base_idx = mid
                base_val = nums[mid]
                break
            else:
                if nums[mid] > nums[r]:
                    l = mid + 1
                elif nums[mid] < nums[l]:
                    r = mid - 1
                else:
                    # this is ordered
                    base_idx = l
                    base_val = nums[l]
                    break
        
        if base_idx == None:
            base_idx = mid
            base_idx = nums[mid]

        if target >= nums[0]:
            l = 0
            r = base_idx - 1
            if r < 0:
                r = N - 1
        else:
            l = base_idx
            r = N - 1
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1


