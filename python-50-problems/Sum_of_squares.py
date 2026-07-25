from datetime import datetime

class SumOfSquares:
    def __init__(self,n):
        self.n=n
    def __str__(self):
        return f"{self.n} -> {self.compute()}"
    def compute(self):
        n=self.n
        s=0
        for i in range(len(n)):
            s+=n[i]*n[i]
        return s




print(f"=== Run: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ===")
print(SumOfSquares([1, 2, 3]))   # [1, 2, 3] -> 14
print(SumOfSquares([0, 5]))      # [0, 5] -> 25
print(SumOfSquares([]))           # [] -> 0
print(SumOfSquares([-3, 4]))      # [-3, 4] -> 25   <- отрицательные тоже квадратятся честно