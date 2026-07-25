from datetime import datetime

class EvenOddCheck:
    def __init__(self,n):
        self.n=n

    @property
    def n(self):
        return self._n

    @n.setter
    def n(self,n):
        if not isinstance(n,int):
            raise TypeError("n must be an integer")
        self._n=n
        
    def __str__(self):
        return "EVEN" if self.is_even() else "ODD"

    def is_even(self):
        if self.n %2==0:
            return True
        else: 
            return False
    

print(f"=== Run: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ===")
print(EvenOddCheck(7))    # ODD
print(EvenOddCheck(4))    # EVEN
print(EvenOddCheck(0))    # EVEN
print(EvenOddCheck(-3))   # ODD