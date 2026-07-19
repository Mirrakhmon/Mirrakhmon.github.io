from datetime import datetime


class Time:
    def __init__(self,h,m):
        self.h=h
        self.m=m
    def __str__(self):
        return f"{self.h} h {self.m} min"
    def __add__(self, other):
        h = self.h + other.h
        m = self.m + other.m
        if m>=60:
            h+=1
            m-=60
        return Time(h,m)
    def __eq__(self,other):
        c=(self.h == other.h) and (self.m == other.m)
        return c


print(f"=== Запуск: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ===")
print(Time(1, 40) + Time(2, 55))    # 4 h 35 min
print(Time(1, 30) + Time(1, 30))    # 3 h 0 min  ← новый
print(Time(2, 30) == Time(2, 30))   # True
print(Time(2, 30) == Time(2, 31))   # False