import re
name = str(input("Enter the name : "))
regex_name = "^[A-Z][a-z]{15}+$"
if re.match(regex_name,name):
    print(name)
else:
    print("enter name again")


# Revision all - 15-01-26