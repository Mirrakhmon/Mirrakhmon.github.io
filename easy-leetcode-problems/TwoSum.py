class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            k=0
            n=x
            while n>0:
                k=k*10+n%10
                
                n=n//10
            if x==k:
                return True
            else:
                return False

sol = Solution()
print(sol.isPalindrome(121))    # True
print(sol.isPalindrome(-121))   # False
print(sol.isPalindrome(10))     # False
print(sol.isPalindrome(0))      # True