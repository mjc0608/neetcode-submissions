import copy

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        bs = k

        l2r = copy.deepcopy(nums)
        r2l = copy.deepcopy(nums)
        while len(l2r) % bs != 0:
            l2r.append(l2r[-1])
            r2l.append(r2l[-1])
        # print("num", nums)

        for i in range((len(nums) - 1) // bs + 1):
            for j in range(1, bs):
                l2r[i*bs+j] = max(l2r[i*bs+j], l2r[i*bs+j-1])
            for j in reversed(range(0, bs-1)):
                r2l[i*bs+j] = max(r2l[i*bs+j], r2l[i*bs+j+1])
        # print("l2r", l2r)
        # print("r2l", r2l)
        
        res = []
        for i in range(0, len(nums) - k + 1):
            res.append(max(r2l[i], l2r[i+k-1]))
        return res