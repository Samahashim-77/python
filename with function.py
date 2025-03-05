with open("f1.txt", "r") as a :
   data= a.readlines()
   for line in data:
      word=line.split()
      print(word) 
a.close()
file = open ("m2.txt", "x")
import os
if os.path.exists("m2.txt"):
   print("file exists")
else:
   print("not exists")
os.remove("m2.txt")
os.rmdir("C:\Users\msi\Desktop\python\Hummam")
