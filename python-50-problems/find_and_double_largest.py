from datetime import datetime
class DoubleLargest:
    def __init__(self,n):
        self.n=n
    def __str__(self):
        x=self.find_largest()
        return f"Largest = {x[0]} at index {x[1]}\nArray:{self.double_largest()}"
    def find_largest(self):
        n=self.n
        biggest=n[0]
        bindex=0
        for i in range(len(n)):
            if n[i]>biggest:
                biggest=n[i]
                bindex=i
        return biggest,bindex
    def double_largest(self):
        x=self.find_largest()
        n=self.n.copy()
        n[x[1]]=n[x[1]]*2
        return n

print(f"=== Run: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ===")
print(DoubleLargest([4, 12, 7, 9, 3, 15, 8]))
# Largest = 15 at index 5
# Array: 4 12 7 9 3 30 8

print(DoubleLargest([5]))
# Largest = 5 at index 0
# Array: 10