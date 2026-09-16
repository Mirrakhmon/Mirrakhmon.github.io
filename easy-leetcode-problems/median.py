from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        k=len(nums1)+len(nums2)
        i,j=0,0
        cur,prev=0,0
        for _ in range(k//2+1):
            prev=cur
            if j==len(nums2):
                cur=nums1[i]
                i+=1
            elif i==len(nums1):
                cur=nums2[j]
                j+=1
            elif nums1[i]<=nums2[j]:
                cur=nums1[i]
                i+=1
            else:
                cur=nums2[j]
                j+=1
        if k%2!=0:
            return cur
        return (prev+cur)/2


TESTS = [
    ([1, 3], [2], 2.0),
    ([1, 2], [3, 4], 2.5),
    ([], [1], 1.0),
    ([1, 2, 3], [4, 5, 6], 3.5),
    ([4, 5, 6], [1, 2, 3], 3.5),
]

if __name__ == "__main__":
    solver = Solution()
    for nums1, nums2, expected in TESTS:
        try:
            actual = solver.findMedianSortedArrays(nums1, nums2)
            mark = "OK  " if actual == expected else "FAIL"
        except Exception as error:
            actual = f"{type(error).__name__}: {error}"
            mark = "ERR "
        print(f"{mark} {nums1} {nums2} -> {actual} (expected {expected})")