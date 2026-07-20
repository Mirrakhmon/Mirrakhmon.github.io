from datetime import datetime

class Word:
    def __init__(self,n):
        self.original=n
        self.n=n.lower() 
    def __str__(self):
        return f"{self.original} → {'Palindrome' if self.is_palindrome() else 'Not Palindrome'}"
    def is_palindrome(self):
        n=self.n

        for i in range(len(n)//2):
            if n[i]!=n[-i-1]:
                return False
        return True
    def count_vowels(self):
        n=self.n
        k=0
        for letter in n:
            if letter in "aeiou":      # смотрим только на букву в руке
                k += 1
        return k


        
            
print(Word("Racecar"))                      # Racecar → Palindrome
print(Word("hello"))                        # hello → Not Palindrome
print(Word("ab"))
print(Word("hello").is_palindrome())        # False
print(Word("Education").count_vowels())     # 5



print(f"=== Run: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ===")


