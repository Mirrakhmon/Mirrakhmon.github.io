from datetime import datetime

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs)==0:
            return ""
        b =strs[0]  
        for i in range(len(b)):
            for w in strs[1:]:
                if i==len(w) or w[i]!= b[i]:
                    return b[0:i]
        return b


print(f"=== Run: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ===")
sol = Solution()
print(sol.longestCommonPrefix(["flower", "flow", "flight"]))   # fl
print(sol.longestCommonPrefix(["dog", "racecar", "car"]))       # (пусто)
print(sol.longestCommonPrefix(["interspecies", "interstellar", "interstate"]))  # inters
print(sol.longestCommonPrefix(["a"]))                              # a