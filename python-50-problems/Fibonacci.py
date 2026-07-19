class Fibonacci:
    def __init__(self,n):
        self.n=n
    
    @property
    def n(self):
        return self._n

    @n.setter
    def n(self, value):
        if not isinstance(value, int):
            raise TypeError("n must be int")
        if value >= 0:
            self._n = value 
        else:
            raise ValueError("n cannot be negative")
        
    def __str__(self):
        return f"{self.generate()}"
    def generate(self):
        n=self.n
        f=0
        s=1
        t=0
        summon="0, 1"
        if n>2:
            for i in range(n-2):
                t=f+s
                summon=summon+", "+str(t)
                f=s
                s=t
            return summon
        elif n==1:
            return "0"
        elif n==2:
            return "0, 1"
        else:
            return "(empty)"

print(Fibonacci(10))   # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
print(Fibonacci(1))    # 0            ← граница!
print(Fibonacci(2))    # 0, 1         ← граница!
print(Fibonacci(0))    # (empty)      ← самая коварная граница