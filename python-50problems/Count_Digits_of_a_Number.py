from datetime import datetime

class DigitCounter:
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
        return f"Digit count = {self.count_digits()}"
    
    def count_digits(self):
        n=self.n
        counter=0
        if n!=0:
            while n>0:
                n=n//10
                counter+=1
            return counter
        else:
            return 1
        
print(f"=== Run: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ===")
print(DigitCounter(70235))   # Digit count = 5
print(DigitCounter(7))       # Digit count = 1
print(DigitCounter(0))       # Digit count = 1   <- особый случай!