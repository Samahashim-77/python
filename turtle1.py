
while True:
  while True:
    try :
     first_number = float(input("enter first number: "))
     break
    except ValueError:
    
      input("invalid input. please enter vaild number")

operation = input("enter operation type: ")
second_number = float(input("enter second number: "))
if operation == "+":
      result first_number + second_number
      elif operation  == "-":
       result first_number - second_number 
elif operation  == "/":
     result first_number / second_number 
else:
     result = None
if result != None:
      print(result)

 
repeat = input("do you want to perform another operation(y/n): ")
if repeat == "n":
 break   
   
print("program is exited")








