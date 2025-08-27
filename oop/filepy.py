with open("test.txt","w") as f:

     f.write("print('Hello Nila')\n")
     f.write("Hey, My Code Queen.\n")


with open("test.txt", "r") as f:
     result = f.read()
     print(result)


with open("test.txt", "a") as f:
     f.write("Adding New File.\n")


with open("test.txt", "r") as f:
     result = f.read()
     print(result)


import os
if os.path.exists("nila.py"):
     os.remove("nila.py")
     print("Print File Deleted")
else:
     print("File Not Found!")