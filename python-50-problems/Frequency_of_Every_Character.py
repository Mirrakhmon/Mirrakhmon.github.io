from datetime import datetime

class CharFrequency:
    def __init__(self,word):
        self.word=word
    def __str__(self):
        return f"{self.word} -> {self.count_all()}"
    def count_all(self):
        word=self.word
        freq={}
        for letter in word:
            if letter in freq:
                freq[letter]+=1
            else:
                freq[letter]=1
        return freq
        

print(f"=== Run: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ===")
print(CharFrequency("hello"))
print(CharFrequency("banana"))
print(CharFrequency(""))