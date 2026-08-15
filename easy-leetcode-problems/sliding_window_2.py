from datetime import datetime

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        if k>len(nums):
            raise ValueError("array is shorter than target")

        window_sum=sum(nums[0:k])
        max_sum=window_sum

        for right in range(k,len(nums)):
            window_sum=window_sum+nums[right]-nums[right-k]
            if window_sum>max_sum:
                max_sum=window_sum
        return max_sum/k



print(f"=== Run: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ===")
sol = Solution()
print(sol.findMaxAverage([1, 12, -5, -6, 50, 3], 4))    # 12.75
print(sol.findMaxAverage([5], 1))                          # 5.0
print(sol.findMaxAverage([0, 4, 0, 3, 2], 1))               # 4.0
print(sol.findMaxAverage([-1, -2, -3], 2))                   # -1.5