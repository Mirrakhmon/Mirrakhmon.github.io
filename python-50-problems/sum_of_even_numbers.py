from datetime import datetime

class SumOfEvens:
    def __init__(self,n):
        self.n=n
    def __str__(self):
        return f"Sum of evens = {self.compute()}"
    def compute(self):
        n=self.n
        k=0
        for i in range(1,n+1):
            if i%2==0:
                k+=i
        return k
print(f"=== Run: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ===")
print(SumOfEvens(10))    # Sum of evens = 30    (2+4+6+8+10)
print(SumOfEvens(1))     # Sum of evens = 0      <- граница: чётных чисел нет вообще
print(SumOfEvens(2))     # Sum of evens = 2      <- граница: единственное чётное число
print(SumOfEvens(0))     # Sum of evens = 0      <- граница: диапазон пуст