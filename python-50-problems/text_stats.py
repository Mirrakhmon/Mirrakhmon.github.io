from datetime import datetime

class TextStats:
    def __init__(self, text):
        self.text = text

    def analyze(self):
        stats = {"uppercase": 0, "lowercase": 0, "digits": 0, "other": 0}
        for char in self.text:
            if char.isupper():
                stats["uppercase"] += 1
            elif char.islower():
                stats["lowercase"] += 1
            elif char.isdigit():
                stats["digits"] += 1
            else:
                stats["other"] += 1
        return stats

    def __str__(self):
        s = self.analyze()
        return f"uppercase: {s['uppercase']}, lowercase: {s['lowercase']}, digits: {s['digits']}, other: {s['other']}"


print(f"=== Run: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ===")
print(TextStats("Hello World 123!"))
print(TextStats("HELLO"))
print(TextStats(""))