import re 
pattern = r'a+\.b'
text = 'a.b'
matches = re.fullmatch(pattern,text)
if matches:
    print("valid")
else:
    print("invalid")