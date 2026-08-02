class MultTable:
    def __init__(self, n):
        self.n = n

    def __str__(self):
        return self.output()
    
    def output(self):
        n=self.n
        lines=[]
        for i in range(1,11):
            lines.append(f"{n} * {i} = {n*i}")   
        return "\n".join(lines)



print(MultTable(5))    # должна напечататься вся таблица
print(MultTable(7))    # и для 7 работает без изменений кода