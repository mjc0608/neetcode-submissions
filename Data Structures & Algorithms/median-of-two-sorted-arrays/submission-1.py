class Solution:
    def findKth(self, A, B, AL, BL, k):
        if AL == len(A):
            return B[BL+k-1]
        elif BL == len(B):
            return A[AL+k-1]
        elif k == 1:
            if A[AL] < B[BL]:
                return A[AL]
            else:
                return B[BL]
        else:
            # k must > 1
            k2 = k // 2
            k2 = min(k2, len(A) - AL)
            k2 = min(k2, len(B) - BL)
            if A[AL+k2-1] < B[BL+k2-1]:
                # A's cursor is smaller, A's cut is valid
                return self.findKth(A, B, AL + k2, BL, k - k2)
            else:
                return self.findKth(A, B, AL, BL + k2, k - k2)


    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        k = (len(nums1) + len(nums2))

        if k % 2 == 0:
            k1 = k // 2
            k2 = k // 2 + 1
            return (
                self.findKth(nums1, nums2, 0, 0, k1) +
                self.findKth(nums1, nums2, 0, 0, k2)
            ) / 2
                
        else:
            return float(self.findKth(nums1, nums2, 0, 0, k // 2 + 1))