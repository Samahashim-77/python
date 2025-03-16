new_file= open('New_File.txt', 'x')
new_file.close()
import os
print("Checking if my_file exists or not......")
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("the file does not exist")

my_file =open('my file.txt',"w" )
my_file.write("HI! I am Sama and I am 45 yr old.")
my_file.close()
os.remove('f1.txt')
