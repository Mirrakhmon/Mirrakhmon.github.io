from datetime import datetime
class CharCount: 
    def __init__(self,word,character):
        self.word=word
        self.character=character
    def __str__(self):
        return f"'{self.character}' in \"{self.word}\" -> {self.count()}"
    def count(self):
        w=self.word
        c=self.character
        k=0
        for letter in w:
            if letter==c:
                k+=1
        return k
            
print(f"=== Run: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ===")
print(CharCount("programming", "r"))   # 'r' in "programming" -> 2
print(CharCount("hello", "z"))         # 'z' in "hello" -> 0
print(CharCount("banana", "a"))        # 'a' in "banana" -> 3
print(CharCount("", "x"))              # 'x' in "" -> 0