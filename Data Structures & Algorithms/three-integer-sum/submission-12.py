class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        res = []
        for k in range(0, len(nums)-2):
            i = k + 1
            j = len(nums) - 1

            if nums[k] > 0:
                break

            if k >= 1 and nums[k-1] == nums[k]:
                continue

            target = -nums[k]
            while i < j:
                while nums[i] + nums[j] > target and i < j:
                    j -= 1
                while nums[i] + nums[j] < target and i < j:
                    i += 1

                if nums[i] + nums[j] == target and i != j:
                    res.append([nums[k], nums[i], nums[j]])
                    j -= 1
                    while i < j and nums[j] == nums[j+1]:
                        j -= 1
        return res