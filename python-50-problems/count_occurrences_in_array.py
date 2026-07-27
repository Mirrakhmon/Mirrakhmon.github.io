from datetime import datetime
class OccurrenceCounter:
    def __init__(self,arr,target):
        self.arr=arr
        self.target=target
    def __str__(self):
        return f"Target: {self.target} Occurrences = {self.count()}"
    def count(self):
        a=self.arr
        target=self.target
        x=0
        for i in a:
            if i==target:
                x+=1
        return x
    
print(f"=== Run: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ===")
print(OccurrenceCounter([4, 7, 4, 2, 4, 9, 1, 4], 4))   # Occurrences = 4
print(OccurrenceCounter([1, 2, 3], 5))                    # Occurrences = 0
print(OccurrenceCounter([], 4))                            # Occurrences = 0