from datetime import datetime

class RangeSum:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __str__(self):
        return f"Sum = {self.compute()}"

    def compute(self):
        a=self.a
        b=self.b
        s=0
        for i in range(a,b+1):
            s+=i
        return s



print(f"=== Run: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ===")
print(RangeSum(3, 7))    # Sum = 25
print(RangeSum(5, 5))    # Sum = 5    <- граница: один элемент
print(RangeSum(-2, 2))   # Sum = 0    <- отрицательные тоже суммируются