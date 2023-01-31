# Way 1 :- String formatting with format() method
letter = "Het my name is {} and I'm living in {}"
Name = "Adarsh"
country = "India"
print(letter.format(Name,country))

# Way 2:- String formatting with format() method with the help of Indexing
    # Example 1
letter2 = "Het my name is {1} and I'm living in {0}"#Here in curly braces it will take value very first according to the print statement so.{0} will fill out first and {1} will fill out at last.
Name2 = "Deepanshu"
State = "Haryana"
print(letter2.format(State,Name2))
    # Example 2
Letter3 = "I Live in {1} and My name is {0}"
Name3 = "Sopnil"
place = "Dadri"
print(Letter3.format(Name3,place))

# For doing this in a simpler way we use f-strings

# 1st way
Dollar = 200
print(f"The amount of 1 Dollar in India is Rs.70 .So, the {Dollar} Dollar in India is Rs {Dollar * 70}")#Here we use just f"String" to format this line whatever we want to format we just type that object in {Curly braces} and can print the object .Also can perform Mathmatical operations also.

#2nd way
money = "I have {amt:.3f} rupees in my pocket"#Here with the help of colon : we can also Tell the program that after Decimal (Money:.2f) print 2 values only.
print(money.format(amt = 45.3443))

#3rd way
cash = 2223.43
txt = f"I have {cash:.2f} Dollars! in my bag pack!"
print(txt)


#We can simply make integer into strings performing calculations in it.

print(f"{2 * 30}")
print(type(f"{2 * 30}"))#Its ok that we are performing calculations but the type f-string is always string.Not the integer.

#We dont want to format just we want to show the user that here we have to write. So it is closed with the help if Double curly braces.
print(f"My  name is {{name}} and I live in {{country}}")
