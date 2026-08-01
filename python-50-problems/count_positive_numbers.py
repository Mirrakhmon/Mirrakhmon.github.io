from datetime import datetime
class PositiveCounter:
    def __init__(self,n):
        self.n=n
    def __str__(self):
        return f"Positive count = {self.count_positive()}"
    def count_positive(self):
        n=self.n
        return sum(1 for x in n if x>0)
print(f"=== Run: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ===")
print(PositiveCounter([-3, 5, -8, 2, 0, 7, -1, 4]))   # Positive count = 4
print(PositiveCounter([0, 0, 0]))                       # Positive count = 0
print(PositiveCounter([1, 2, 3]))                       # Positive count = 3