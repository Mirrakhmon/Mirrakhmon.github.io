from datetime import datetime
class SumAverage:
    def __init__(self,n):
        self.n=n
    def __str__(self):
        if self.n:
            return f"Sum = {self.total()}, Average = {self.average()}"
        else: return self.average()
    def total(self):
        n=self.n
        return sum(n)
    def average(self):
        n=self.n
        if self.n:
            return sum(n)/len(n)
        else: 
            return "What to do with empty"
print(f"=== Run: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ===")
print(SumAverage([10, 20, 30, 40, 50, 60, 70, 80]))   # Sum = 360, Average = 45.0
print(SumAverage([5]))                                  # Sum = 5, Average = 5.0
print(SumAverage([]))                                    # что делать с пустым?