from datetime import datetime
class BubbleSorter:
    def __init__(self,n):
        self.n=n
    def __str__(self):
        return f"Sorted: {self.sort()}"
    def sort(self):
        n=self.n.copy()
        if n ==[]:
            return "(Empty)"
        for i in range(len(n)-1):
            for j in range(len(n)-1-i):
                if n[j]>n[j+1]:
                    n[j],n[j+1]=n[j+1],n[j]
        return n
print(f"=== Run: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ===")
print(BubbleSorter([5, 2, 8, 1, 9, 3]))   # Sorted: 1 2 3 5 8 9
print(BubbleSorter([1]))                    # Sorted: 1
print(BubbleSorter([3, 2, 1]))              # Sorted: 1 2 3
print(BubbleSorter([]))                      # Sorted: (пусто)