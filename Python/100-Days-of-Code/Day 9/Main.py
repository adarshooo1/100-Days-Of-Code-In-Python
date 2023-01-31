a = "1"
b = "2"

print(a +b)# here it is printing like a string .

c = (int(a) + int(b))#Here we cast the type Sting to Integer.

print(c)# Here it print the value of type Integer and now it will remain same as Integer.

print(type(c))#Now it is the type of Integer.

print(int(a) + int(b)) #Now it acting like a string just because we cast the type of the value.

print(type(a)) #But still the type of the object is <class 'Str'>

# It doesn't mean that it will change the type of the object completely, object should be valid to get changed ""


Num  = 20
Num2 = 33
ans = (Num +float(Num2))# Here we type cast the value of the integer Datatype to the float Datatypes.
print(type(ans))
print(ans)

age = input("Enter your age:-")
message = f"I am {age} years old."
print(message)  # Output: "I am {age} years old."
print(type(message))
