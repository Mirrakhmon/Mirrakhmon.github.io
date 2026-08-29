class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i]<9:
                digits[i]+=1
                return digits
            else:
                digits[i]=0
        return [1] + digits

        


sol = Solution()
print(sol.plusOne([1, 2, 3]))    # [1, 2, 4]
print(sol.plusOne([9, 9]))        # [1, 0, 0]
print(sol.plusOne([0]))            # [1]