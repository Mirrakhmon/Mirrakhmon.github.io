from datetime import datetime

class Solution:
    def romanToInt(self, s: str) -> int:
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sumr=0
        for index,numb in enumerate(s):
            if index < len(s) - 1 and values[numb] < values[s[index+1]]:
                sumr -= values[numb]
            else:
                sumr += values[numb]
        return sumr


print(f"=== Run: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ===")
sol = Solution()
print(sol.romanToInt("IV"))       # 3
print(sol.romanToInt("LVIII"))      # 58
print(sol.romanToInt("MCMXCIV"))    # 1994