from datetime import datetime

class NumberList: 
    def __init__(self, numbers):
        self.numbers=numbers
    @property
    def numbers(self):
        return self._numbers




    @numbers.setter
    def numbers(self, numbers):
        if not isinstance(numbers, list):
            raise TypeError("n must be list")
        if len(numbers) >= 2:
            self._numbers=numbers
        else:
            raise ValueError("need at least 2 elements")
    
    
    
    def __str__(self):
        return f"second largest: {self.second_largest()}"
    def second_largest(self):
        n=self.numbers
        best=n[0]
        second_best=n[1]
        for i in range(len(n)):
            if n[i]>best:
                best=n[i]
        for i in range(len(n)):
            if n[i] != best and n[i] > second_best:
                second_best = n[i]
        return second_best


print(f"=== Run: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ===")
print(NumberList([10, 5, 20, 8, 20]))    # second largest: 10
print(NumberList([7, 1]))                # second largest: 1
print(NumberList([100, 90, 90, 80]))     # second largest: 90
print(NumberList([-5, -10, -3]))   # second largest: -5