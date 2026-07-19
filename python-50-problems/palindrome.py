class Word:
    def __init__(self,word):
        self.original = word
        self.word=word.lower()
    def __str__(self):
        if self.is_palindrome() is True:
            return f"{self.original} → Palindrome"
        else:
            return f"{self.original} → Not Palindrome"
    def count_vowels(self):
        ch=self.word
        c=0
        for i in range (len(ch)):
            if ch[i] in "aeiou":
                c+=1
        return c


    def is_palindrome(self):
        x=self.word
        k=len(x)-1
        m=1
        for i in range(k//2+1):
            if x[i]==x[k-i]:
                m=m*1
            else:
                m=m*0
        if m==1:
            return True
        else:
            return False
        
print(Word("Racecar"))   # racecar → palindrome
print(Word("hello"))     # hello → not palindrome
print(Word("a"))         # a → palindrome
print(Word("noon"))      # noon → palindrome
print(Word("hello").is_palindrome())  

print(Word("programming").count_vowels())   # 3
print(Word("sky").count_vowels())           # 0
print(Word("Education").count_vowels())     # 5
print(Word("aeiouAEIOU").count_vowels())    # 10
        