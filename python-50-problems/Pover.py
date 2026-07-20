from datetime import datetime

class Power_hand:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __str__(self):
        return f"{self.a}^{self.b} = {self.compute()}"
    def compute(self):
        a=self.a
        b=self.b
        k=1
        for i in range(b):
            k*=a
        return k
print(f"=== Run: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ===")
print(Power_hand(2, 10))   # 2^10 = 1024
print(Power_hand(5, 3))    # 5^3 = 125
print(Power_hand(7, 0))    # 7^0 = 1     <- edge case
print(Power_hand(1, 100))  # 1^100 = 1
print(Power_hand(0, 5))    # 0^5 = 0