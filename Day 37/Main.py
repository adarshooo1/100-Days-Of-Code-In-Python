# Question:- Create a list and Take Input from user.If the input is == any item in the list then print
# the index with the Item other wise through message that Input from user is not present in the list.
# If the Input by user is other than required Dayatype then print a value error.
# In last when program get over with the keyword Finally in program print a message "Program executed".

inp = input("Enter the number searching in the list:-")
Lst = [20,30,24,22,13,18,200,786]
flag = False#This will set a parameter to the program to run
try:
   for i in Lst:
      if(int(inp) == i):
         flag = True
         print(f"Input number is {inp} and Number Found at index {Lst.index(i)}")  
   if not flag:
      print(f"Number {inp} not found") 
except ValueError:#It will raise the value error if the input is other than the required Datatype.
   print("Enter the Input in Integer")
finally:#This will execute at every condition.
   print("Program Executed!")