import re

email=input("Enter your email address: ").strip()

if re.search(".+@.+", email):
    print("Valid email address.")
else:
    print("Invalid email address.")