from datetime import datetime
class MinFinder:
    def __init__(self,n):
        self.n=n
    def __str__(self):
        return f"Minimum = {self.find_min()}"
    def find_min(self):
        n=self.n
        the=n[0]
        for x in n:
            if the>=x:
                the=x
        return the
print(f"=== Run: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ===")
print(MinFinder([12, 5, 8, 3, 15, 7]))   # Minimum = 3
print(MinFinder([7]))                     # Minimum = 7
print(MinFinder([-5, -10, -3]))           # Minimum = -10