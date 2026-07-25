from datetime import datetime

class ReverseArray:
    def __init__(self,n):
        self.n=n
    def __str__(self):
        return f"{self.n} -> {self.reverse()}"
    def reverse(self):
        n=self.n
        k=[]
        for i in range(len(n)):
            k.append(n[-i-1])
        return k

print(f"=== Run: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ===")
print(ReverseArray([1, 2, 3, 4, 5]))   # [1, 2, 3, 4, 5] -> [5, 4, 3, 2, 1]
print(ReverseArray([10, 20]))          # [10, 20] -> [20, 10]
print(ReverseArray([]))                 # [] -> []
print(ReverseArray([7]))                # [7] -> [7]