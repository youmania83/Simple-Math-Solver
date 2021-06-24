

import math 
print("Welcome to the simple math helper")
while True:
  Question=int(input('''What would you like to calculate?
  1. Sqrt
  2. Log
  3. Factorial''''\n'))
  if Question == 1:
    num=int(input("Enter the number to sqrt "))
    print (f"The sqrt of {num} is : ",end="")
    print(math.sqrt(num))
  elif Question == 2:
    num=int(input("Enter the number to log "))
    print (f"The log of {num} is : ",end="")
    print (math.log(num))
  elif Question == 3:
    num=int(input("Enter the number to fact "))
    n = num
    fact = 1
    
    for i in range(1,n+1):
        fact = fact * i
          
    print (f"The factorial of {Question} is : ",end="")
    print (fact)    