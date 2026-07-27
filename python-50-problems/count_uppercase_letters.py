from datetime import datetime

class UppercaseCounter:
    def __init__(self,n):
        self.n=n
    def __str__(self):
        return f"Uppercase: {self.analyze()}"
    def analyze(self):
        n=self.n
        a=[]
        for x in n:
            if x.isupper():
                k+=1
        return k

print(f"=== Run: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ===")
print(UppercaseCounter("HelloWorld"))   # Uppercase: 2
print(UppercaseCounter("hello"))        # Uppercase: 0
print(UppercaseCounter("HELLO"))        # Uppercase: 5
print(UppercaseCounter(""))              # Uppercase: 0