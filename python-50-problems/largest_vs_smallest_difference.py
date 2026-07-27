from datetime import datetime
class RangeDifference:
    def __init__(self,n):
        self.n=n
    @property
    def n(self):
        return self._n
    @n.setter
    def n(self,n):
        if not isinstance(n,list):
            raise TypeError("n must be list")
        if len(n)>0:
            self._n=n
        else:
            raise ValueError("need at least one element in list")
    def __str__(self):
        summing=self.difference()
        return f"{self.n} → Difference = {(summing[0]-summing[1])}   ({summing[0]} - {summing[1]})"
    def difference(self):
        n=self.n
        biggest=n[0]
        smallest=n[0]
        for i in n:
            if i>=biggest:
                biggest=i
            if i<=smallest:
                smallest=i
        return biggest,smallest
print(f"=== Run: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ===")
print(RangeDifference([14, 3, 22, 7, 18, 9]))   # Difference = 19
print(RangeDifference([5]))                      # Difference = 0   <- один элемент
print(RangeDifference([-10, -3, -7]))            # Difference = 7   <- отрицательные