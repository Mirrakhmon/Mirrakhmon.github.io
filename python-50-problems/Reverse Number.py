from datetime import datetime

class ReverseNumber:
    def __init__(self,n):
        self.n=n
    def __str__(self):
        return f"{self.n} -> {self.compute()}"
    def compute(self):
        n=self.n #n means just a number
        r=0  #r means reverse number
        while n>0:
            r=r*10+n%10
            n=n//10
        return r




print(f"=== Run: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ===")
print(ReverseNumber(521))
print(ReverseNumber(1234))
print(ReverseNumber(7))
print(ReverseNumber(100))
print(ReverseNumber(0))