class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for item in nums:
            if item in s:
                return True
            s.add(item)
        return False