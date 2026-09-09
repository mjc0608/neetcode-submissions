class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[i-1] * nums[i])
        
        postfix = [1 for i in range(len(nums))]
        postfix[len(nums)-1] = nums[len(nums)-1]
        for i in reversed(range(0, len(nums)-1)):
            postfix[i] = postfix[i+1] * nums[i]

        r = []
        for i in range(0, len(nums)):
            k = 1
            if i - 1 >= 0:
                k *= prefix[i-1]
            if i + 1 < len(nums):
                k *= postfix[i+1]
            r.append(k)
        return r