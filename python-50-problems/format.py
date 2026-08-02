import re

name=input("What is your name? ")

if matches:=re.search(r"^(.+), *(.+)$", name):
    print(f"Your first name is {matches.group(2)} and your last name is {matches.group(1)}.")
else:    print("Your name doesn't match the expected format.")