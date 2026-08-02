class Sum_odd:
    def __init__(self,n):
        self.n = n
        self.sumn=0
    def __str__(self):
        return f"Sum of odd numbers {self.sumn}"
    def countodd(self):
        self.sumn=0
        for i in range(1,self.n+1,2):
            self.sumn+=i
class FindMax:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c    
    def fmax(self):
        if(self.a>self.b and self.a>self.c):
            return self.a
        elif(self.b>self.a and self.b>self.c):
            return self.b
        else:
            return self.c
    def __str__(self):
        return f"Maximum = {self.fmax()}"
class DigitSum:
    def __init__ (self,n):
        self.n=n
    def digit_sum(self):
        n=self.n
        total=0
        while n>0:
            total=total+n%10
            n//=10
        return total


    def __str__(self):сщву
        return f"Sum of digits = {self.digit_sum()}"



num = DigitSum(1234)
print(num)               # Sum of digits = 10
print(DigitSum(70235))   # Sum of digits = 17
print(DigitSum(5))       # Sum of digits = 5