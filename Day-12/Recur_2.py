# Regex 
import re
partten =r"^[a-zA-z0-9._%+-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$"

email = "akashtiwari1014@gmailcom"

if re.fullmatch(partten,email):
    print("valid")
else:
    print("invalid")