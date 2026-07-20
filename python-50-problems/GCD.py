from datetime import datetime

class GCD:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __str__(self):
        return f"GCD({self.a}, {self.b}) = {self.compute()}"
    
    def compute(self):
        a=self.a
        b=self.b
        while b!=0:
            a, b = b, a % b
        return a
    
print(f"=== Run: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ===")       
print(GCD(48, 18))    # GCD(48, 18) = 6
print(GCD(7, 13))     # GCD(7, 13)  = 1     <- coprime numbers
print(GCD(10, 10))    # GCD(10, 10) = 10
print(GCD(12, 0))     # GCD(12, 0)  = 12    <- edge case: gcd(n, 0) = n
