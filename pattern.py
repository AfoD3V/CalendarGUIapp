import re
txt = "Programowanie1-,. "
x = re.findall("[a-zA-Z0-9-,. ]", txt)
print(x)

if len(txt) == len(x):
    print("!!!")
