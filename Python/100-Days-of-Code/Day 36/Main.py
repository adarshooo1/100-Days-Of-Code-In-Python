a = input("Enter a number:- ")#If we give input as Integer so it will work but if we 
# give some other input then it will throgh some error
#If the number is valid then it will print table if it enter the other datatype other than integer then print exception.
print(f"Multiplication table of {a} is :-")
try:
  for i in range (1,11):
    print(f"{int(a)} x {i} = {int(a)*i}" )
except Exception as e:
  print(e)
print("Your multiplication table has done\nProgram Ended")

try:
    num = int(input("Enter an Integer:- "))
    a = [2,6]
    print(a[num])
except ValueError :
    print("Number entered is not an Integer") 
except IndexError:
    print("Index Error")

