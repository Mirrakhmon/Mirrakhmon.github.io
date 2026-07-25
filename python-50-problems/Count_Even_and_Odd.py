from datetime import datetime
class EvenOddCounter:
    def __init__(self,n):
        self.n=n
    @property
    def n(self):
        return self._n
    @n.setter
    def n(self,n):
        if not isinstance(n,list):
            raise TypeError("n must be a number")
        self._n=n
    def __str__(self):
        result=self.count()
        return f"even: {result[0]}, odd: {result[1]}"
    def count(self):
        n=self.n
        e=0
        o=0
        for i in n:
            if i%2==0:
                e+=1
            else: 
                o+=1
        return e,o
    
print(f"=== Run: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ===")
print(EvenOddCounter([1, 2, 3, 4, 5, 6]))   # even: 3, odd: 3
print(EvenOddCounter([2, 4, 6]))             # even: 3, odd: 0
print(EvenOddCounter([]))                     # even: 0, odd: 0
print(EvenOddCounter([-3, -4]))               # even: 1, odd: 1  <- отрицательные тоже считаются