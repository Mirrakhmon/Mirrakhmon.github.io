from datetime import datetime

class Deduplicate:
    def __init__(self,n):
        self.n=n
    def __str__(self):
        return f"{self.n} -> {self.remove_duplicates()}"
    def remove_duplicates(self):
        n=self.n
        k=[]
        for i in n:
            if i not in k:
                k.append(i)
        return k

print(f"=== Run: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ===")
print(Deduplicate([1, 2, 2, 3, 1, 4]))   # [1, 2, 2, 3, 1, 4] -> [1, 2, 3, 4]
print(Deduplicate([5, 5, 5, 5]))         # [5, 5, 5, 5] -> [5]
print(Deduplicate([]))                    # [] -> []
print(Deduplicate([1, 2, 3]))             # [1, 2, 3] -> [1, 2, 3]  <- уже уникальны