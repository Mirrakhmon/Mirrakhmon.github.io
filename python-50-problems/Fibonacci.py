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
        if self.n>0:
            return ", ".join(str(x) for x in self.generate())
        else:
            return "(empty)"
    def generate(self):
        result = []
        while len(result) < self.n:
            if len(result)==0:
                result.append(0)
            elif len(result)==1:
                result.append(1)
            else:
                result.append(result[-1] + result[-2])
        return result

print(Fibonacci(10))   # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
print(Fibonacci(1))    # 0            ← граница!
print(Fibonacci(2))    # 0, 1         ← граница!
print(Fibonacci(0))    # (empty)      ← самая коварная граница
#print(Fibonacci(10).generate())    # напечатает None? или список?
print(sum(Fibonacci(10).generate()))