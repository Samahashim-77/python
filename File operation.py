
file_read=open("f1.txt", 'r')
print("file in read mode -")
print(file_read.read())
file_read.close()

file=open("f1.txt", "r")
counter= 0
content =file.read()
colist= content.split("\n")
for i in colist:
    if i:
        counter +=1
print("this is the number of lines in the file")
print(counter)

