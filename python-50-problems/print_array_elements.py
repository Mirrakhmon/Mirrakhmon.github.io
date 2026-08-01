from datetime import datetime
class ArrayPrinter:
    def __init__(self,n):
        self.n=n
    def __str__(self):
        return f"{self.format_output()}"
    def format_output(self):
        n=self.n
        k=" ".join(str(x) for x in n)
        return k

print(f"=== Run: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ===")
print(ArrayPrinter([5, 10, 15, 20, 25]))   # 5 10 15 20 25
print(ArrayPrinter([]))                      # (пусто)
print(ArrayPrinter([7]))                     # 7