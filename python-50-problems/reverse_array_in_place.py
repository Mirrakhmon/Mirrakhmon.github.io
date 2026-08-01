from datetime import datetime
class ArrayReverser:
    def __init__(self,n):
        self.n=n
    def __str__(self):
        return f"Array: {self.reverse_in_place()}"
    def reverse_in_place(self):
        n=self.n.copy()
        i=0
        j=len(n)-1
        while i<j:
            n[i],n[j]=n[j],n[i]
            i+=1
            j-=1
        return n
print(f"=== Run: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ===")
print(ArrayReverser([1, 2, 3, 4, 5]))   # Array: 5 4 3 2 1
print(ArrayReverser([10, 20]))          # Array: 20 10
print(ArrayReverser([7]))               # Array: 7
print(ArrayReverser([]))                 # Array: (пусто)