from datetime import datetime
class TextStats: 
    def __init__(self,text):
        self.text=text
    def __str__(self):
        result=self.analyze()
        return f"uppercase: {result['upe']}, lowercase: {result['lowke']}, digits: {result['digi']}, other: {result['rest']}"
    def analyze(self):
        x=self.text
        stats={"upe":0, "lowke":0,"digi":0,"rest":0}
        for char in x:
            if char.isupper():
                stats["upe"]+=1
            elif char.islower():
                stats["lowke"]+=1
            elif char.isdigit():
                stats["digi"]+=1
            else:
                stats["rest"]+=1
        return stats
print(f"=== Run: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ===")
print(TextStats("Hello World 123!"))
print(TextStats("HELLO"))
print(TextStats(""))