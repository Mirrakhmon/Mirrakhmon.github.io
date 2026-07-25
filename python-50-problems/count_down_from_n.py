from datetime import datetime

class Countdown:
    def __init__(self,n):
        self.n=n
    def __str__(self):
        lines = [str(x) for x in self.run()]
        lines.append("Done!")
        return "\n".join(lines)
    def run(self):
        n=self.n
        k=[]
        for i in range(n, 0, -1):
            k.append(i)
        return k

            

print(f"=== Run: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ===")
print(Countdown(4))
# 4
# 3
# 2
# 1
# Done!