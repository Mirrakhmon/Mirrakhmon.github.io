from datetime import datetime
class StringReverser:
    def __init__(self,text):
        self.text=text
    def __str__(self):
        return f"{self.reverse()}"
    def reverse(self):
        text=self.text
        rtext=""
        for i in range(len(text)-1,-1,-1):
            rtext+=text[i]
        return rtext
print(f"=== Run: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ===")
print(StringReverser("hello"))    # olleh
print(StringReverser("a"))         # a          <- граница: один символ
print(StringReverser(""))           # (пустая строка)  <- граница: пустой ввод
print(StringReverser("racecar"))   # racecar    <- палиндром, развернётся сам в себя