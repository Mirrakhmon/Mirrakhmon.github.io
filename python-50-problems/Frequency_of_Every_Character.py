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
    def most_frequent(self):
        freq = self.count_all()
        best_letter = None
        best_count = 0
        for letter in freq:              # обход ключей словаря
            if freq[letter] > best_count:
                best_count = freq[letter]
                best_letter = letter
        return best_letter, best_count    

print(f"=== Run: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ===")
print(CharFrequency("hello"))
print(CharFrequency("banana"))
print(CharFrequency(""))
print(CharFrequency("hello").most_frequent())    # ('l', 2)
print(CharFrequency("banana").most_frequent())   # ('a', 3)
print(CharFrequency("abc").most_frequent())      # ('a', 1)  <- все равны, берём первого