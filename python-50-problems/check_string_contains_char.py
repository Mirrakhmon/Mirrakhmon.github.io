from datetime import datetime
class CharChecker: 
    def __init__(self,text,k):
        self.text=text
        self.k=k
    def __str__(self):
        return f"{'YES' if self.contains() else 'NO'}"
    def contains(self):
        text=self.text
        k=self.k
        return k in text

print(f"=== Run: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ===")
print(CharChecker("hello", "e"))   # YES
print(CharChecker("hello", "z"))   # NO
print(CharChecker("", "a"))         # NO