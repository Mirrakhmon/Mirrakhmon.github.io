from datetime import datetime

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        slow=0
        for fast in range(1,len(nums)):
            if nums[fast]!=nums[slow]:
                slow+=1
                nums[slow]=nums[fast]
        return slow+1
            




print(f"=== Run: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ===")
sol = Solution()
nums1 = [1, 1, 2]
k1 = sol.removeDuplicates(nums1)
print(k1, nums1[:k1])    # 2 [1, 2]

nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k2 = sol.removeDuplicates(nums2)
print(k2, nums2[:k2])    # 5 [0, 1, 2, 3, 4]