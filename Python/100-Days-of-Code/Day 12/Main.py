Name = "Adarsh Kumar Singh"
# //////////////////////////////////////////////////////////////////////
print("POSITIVE SLICING")
print(len(Name))
print(Name[:])#Here [Starting is not define. So it will automatically take 0: And it takes till len(Name) which is length of the string]
print(Name[0:6])#Here [0:- which is the starting index:6:-Till that index we want to print]
print(Name[:12])#Here it print at the element till 12(n-1).
print(Name[6:len(Name)])#Here it prints from 6th element from the String to the length of the string
print(Name[::2])#Here it print every 2nd element in the String
print(Name[1::2])#Here is starting from 1 and print every 2nd element in the String
# ///////////////////////////////////////////////////////////////////////
print("NEGATIVE SLICING")
print(Name[:-1])#Here it will simply reduce the len-1 and print:-Adarsh Kumar Sing
print(Name[-3:-1])#Here it works like:-[len(Name)-3 = 15:len(Name)-1 = 17] and print the element in between that which start from index 15 and print till 17(n-1).
print(Name[-3:-4])#Here it will print nothing because:- 18-3 = 15:18-4 = 14 which is,[15:14] Hence,No sense.

# ///////////////////////////////////////////////////////////////////////////////////
print("Looping through String")
for char in Name:
    print(char,end = " ",)#Able to print character in the same line through looping with this syntax.

for char2 in Name:
    print(char2)#It will print String every character in a new line
# /////////////////////////////////////
Name2 = "Harry"
print(Name2[-4:-2])
    


