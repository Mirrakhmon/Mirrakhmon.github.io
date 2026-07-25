from datetime import datetime

class TempConverter:
    def __init__(self,C):
        self.C=float(C)
    def __str__(self):
        return f"{self.C}°C = {self.to_fahrenheit()}°F"
    def to_fahrenheit(self):
        return self.C * 9/5 + 32


print(f"=== Run: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ===")
print(TempConverter(25))     # 25.0°C = 77.0°F
print(TempConverter(0))      # 0.0°C = 32.0°F
print(TempConverter(-40))    # -40.0°C = -40.0°F