from datetime import datetime
class Time:
    def __init__(self,h,s):
        self.h=h
        self.s=s
    def __str__(self):
        return f"{self.h} h {self.s} min"
    def __add__(self, other):
        h=self.h+other.h
        s=self.s+other.s
        if s>=60:
            h+=1
            s-=60
        return Time(h,s)
    def __eq__(self,other):
        return self.h==other.h and self.s==other.s
        
print(f"=== Run: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ===")
print(Time(1, 40) + Time(2, 55))    # 4 h 35 min
print(Time(1, 30) + Time(1, 30))    # 3 h 0 min   <- граница: ровно 60 минут
print(Time(2, 30) == Time(2, 30))   # True
print(Time(2, 30) == Time(2, 31))   # False