from datetime import datetime

class Solution:
    def isValid(self, s: str) -> bool:
        checker={'(':')','[':']','{':'}'}
        k=[]
        for char in s:
            if char in checker:
                k.append(char)
            else:
                if k and checker[k[-1]] == char:
                    k.pop()
                else:
                    return False
        return True


print(f"=== Run: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ===")
sol = Solution()
print(sol.isValid("()"))          # True
print(sol.isValid("()[]{}"))       # True
print(sol.isValid("(]"))           # False
print(sol.isValid("([)]"))         # False
print(sol.isValid("{[]}"))         # True


