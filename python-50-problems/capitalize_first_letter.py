from datetime import datetime
class Capitalizer:
    def __init__(self,words):
        self.words=words
    def __str__(self):
        return f"{self.capitalize()}"
    def capitalize(self):
        n=self.words
        k=""
        for i in range(len(n)):
            if i==0 or (n[i-1]==' 'and n[i]!=' '):
                k+=n[i].upper()
            else:
                k+=n[i]
                
        return k


print(f"=== Run: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ===")
print(Capitalizer("hello world foo"))     # Hello World Foo
print(Capitalizer("python"))               # Python
print(Capitalizer(""))                      # (пусто)