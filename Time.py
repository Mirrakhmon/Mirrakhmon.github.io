class Time:
    def __init__(self,hours,minut):
        self.hours = hours
        self.minut = minut


    def __str__(self):
        return f"{self.hours} h {self.minut}min"
    
    def __add__(self, other):
        hours=self.hours+other.hours
        minut=self.minut + other.minut
        if minut>=60:
            hours = hours+1
            minut = minut-60
        return Time(hours,minut)
    def __eq__(self, other):
        verdict= (self.hours == other.hours) and (self.minut == other.minut)
        
        return verdict

Martin=Time(1,40)
Sam=Time(2,55)

_sum=Martin+Sam
print(_sum)
print(Time(2, 30) == Time(2, 30))
print(Time(2, 30) == Time(2, 31))
total = Time(1, 50) + Time(2, 50) + Time(3, 50)
print(total)