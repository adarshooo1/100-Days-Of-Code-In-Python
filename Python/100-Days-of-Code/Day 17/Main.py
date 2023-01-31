# Example 1:- Printing number through looping
for Numbers in range(1,101):#Starting from 1 print till 100.Otherwise if we do not mention then it start from 0 and print till 100.
    print(Numbers)

# Example 2:- Printing character in String through Looping which iterate over the string character. 
for Str in "Adarsh":
    print(Str)#To print all character in new line.
    print(Str,end =' ')#To print all together in a same line with a single space.

# Example 3:- Iterate and print list items type of String using for loop.
Colors = ["Red","Green","Blue","Black","Brown"]   
for color in Colors:
    print(color)
    for char in color:#Nested for loop(Loop inside a loop)
        print(char,end = " ")
    
# Example 4:- Iterate and print list itme type of Integer using for loop.
for nums in [1, 2, 3, 4, 5]:
    print(nums)

#Example 5:- Step in loops
for nums2 in range(0,121,12):#This is named as step in loop which will raise a step after 12 number or whatever the number user want to step.
    print(nums2)
    #Means print num2 staring from 0 to 121 and making a difference between every number is 12.
