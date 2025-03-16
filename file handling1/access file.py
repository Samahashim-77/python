file = open('f1.txt')
print(file.read())
file.close()

file_read= open('f1.txt', 'r')
print("File in Read Mode -")
print(file_read.read())
file_read.close()

file_write = open('f1.txt', 'w')
file_write.write("File in write mode....")
file_write.write("Hi! I am Sama. I am 45 yr. old")
file_write.close()
