from datetime import datetime
class StringUppercaser:
    def __init__(self,n):
        self.n=n
    def __str__(self):
        return f"{self.to_upper()}"
    def to_upper(self):
        return self.n.upper()

print(f"=== Run: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ===")
print(StringUppercaser("hello"))     # HELLO
print(StringUppercaser(""))           # (пусто)