from datetime import datetime
import math

class Prime:
    def __init__(self,n):
        self.n=n
    
    @property
    def n(self):
        return self._n

    @n.setter
    def n(self, value):
        if not isinstance(value, int):
            raise TypeError("n must be int")
        if value >= 0:
            self._n = value 
        else:
            raise ValueError("n cannot be negative")
    def __str__(self):
        if self.is_prime():
            return f"{self.n} → prime"
        else:
            return f"{self.n} → not prime"

    def is_prime(self):
        n=self.n
        if n==0 or n==1:
            return False
        for i in range(2, math.isqrt(n) + 1):
            if n%i==0:
                return False
        return True


print(f"=== Run: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ===")

print(Prime(7))      # 7 → prime
print(Prime(12))     # 12 → not prime
print(Prime(2))      # 2 → prime
print(Prime(1))      # 1 → not prime   ← граница №1
print(Prime(0))      # 0 → not prime   ← граница №2
print(Prime(97))     # 97 → prime
print(Prime(25))     # что скажет ваш код?
print(Prime(49))     # а тут?