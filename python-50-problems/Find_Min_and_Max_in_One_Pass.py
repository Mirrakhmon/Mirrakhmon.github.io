from datetime import datetime

class MinMax:
    def __init__(self,n):
        self.n=n
    def __str__(self):
        result= self.find_min_max()
        return f"min: {result[0]}, max: {result[1]}"
    def find_min_max(self):
        n=self.n
        mi=n[0]
        mx=n[0]
        for i in n:
            if i<=mi:
                mi=i
            if i>=mx:
                mx=i
        return mi,mx
print(f"=== Run: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ===")
print(MinMax([5, 3, 8, 1, 9, 2]))   # min: 1, max: 9
print(MinMax([7]))                   # min: 7, max: 7
print(MinMax([-3, -10, -1]))         # min: -10, max: -1