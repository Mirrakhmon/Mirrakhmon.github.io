from datetime import datetime

class Average:
    def __init__(self,n):
        self.n=n
    @property
    def n(self):
        return self._n
        
        
        
        
    @n.setter
    def n(self, n):
        if not isinstance(n, list):
            raise TypeError("n must be a number")
        self._n=n
        if len(n):
            self._n=n
        else:
            raise ValueError("need at least 1 elements")
    def __str__(self):
        return f"{self.n} ->{self.compute()}"
    def compute(self):
        n=self.n
        return sum(n)/len(n)
print(f"=== Run: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ===")
print(Average([1, 2, 3, 4, 5]))   # [1, 2, 3, 4, 5] -> 3.0
print(Average([10, 20]))          # [10, 20] -> 15.0
print(Average([7]))               # [7] -> 7.0
print(Average([]))                 # что делать с пустым списком?