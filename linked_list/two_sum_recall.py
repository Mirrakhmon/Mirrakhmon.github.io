class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen={}
        for i, num in enumerate(nums):
            diff=target-num
            if diff in seen:
                return [seen[diff],i]
            seen[num]=i
        return []


sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))    # [0, 1]
print(sol.twoSum([3, 2, 4], 6))          # [1, 2]
print(sol.twoSum([3, 3], 6))              # [0, 1]