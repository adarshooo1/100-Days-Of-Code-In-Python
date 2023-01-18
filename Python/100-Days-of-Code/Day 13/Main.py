Str = "Black Box"
print(Str)

print(len(Str))#It gives length of the String (n-1).

#.upper()
print(Str.upper())#It will print is Upper Case
print(Str)

#.lower()
print(Str.lower())#It will print in Lower Case
print(Str)

# islower()
print(Str.islower())#It will Return Boolen if The character is all Lower case.

# isupper()
print(Str.isupper())#It will Return Boolen if The character is all Upper case.

#.rstrip(//)
Str2 = "Hurrah!!!!!!!!!!!!!!!!!!!"
print(Str2.rstrip("!"))#It will remove the character which is the last end only which is single and group of same character
   #Both of the strip functions below get fail because rstrip() do not remove the First character as well as repetative character in the string only the last character or the group of last charater is same.
Str3 = "Mayankkkkku"
print(Str3.rstrip("M"))
print(Str3.rstrip("k"))

#replace(//,//)
Str4 = "Adarsh"
print(Str4.replace("Adarsh","Dhruv"))#It can replace like this as well as from a sentence also

# split()
Str5 = "Adarsh Kumar Singh"
print(Str5.split(" "))#It makes a string into a list. But, //Condition is String or Sentence have space between in it to convert into a list
print(type(Str5.split(" ")))

# Capitalize()
Str6 = "GAME CHANGER"
print(Str6.capitalize())#It wil convert only first letter in uppercase() else remaining all in lowercase(), even though whatever the String type is.

# center()
Str7 = "G.O.A.T"
print(Str7.center(20))#It just center the String according to the parameter given by proframmer.

# count()
Str8 = "Adarsh"
print(Str8.count("a"))#It will just count the occurance of the character in String.
print(Str8.lower().count("a"))#First convert to lower case then count the character
print(Str8.upper().count("A"))#First convert to upper case then count the character

# endswith()
Str9 = "Goose in the Bombs"
print(Str9.endswith("s"))#It just checking and return in the Boolean Exprassion:-(True & False) So.True
print(Str9.endswith("Bombs"))#So,True
print(Str9.endswith("b"))#So, False
print(Str9.endswith("in",5,8))#So it is also true parameter wise.

# find()
Str10 = "Saturday Nights and Sunday Morning are the most enjoyable time for everyone"
print(Str10.find("Morning"))#It will find the word and Tell the Index of the Character in the String also only the very first occurance of the character.
print(Str10.find("to"))#If the String is not findable then it will return -1.(Not Existing)

# index()
Str11  = "Hello:- Mr. Adarsh"
print(Str11.index("Mr"))#It is same as find() but difference is It will raise a Error in program of the Keyowrd is Missing in the Error.Example:- Before Printing anyone name is Mr. is available in String or Not is yes then print.If no then Raise a Error
Str11a = "Hello :- aMr Adarsh"
print(Str11a.index("Mr"))#It will also return index if the Character we enter is similar with a big String which has all the character in it that we are finding. Ex:- Finding: Mr String:Mrahana. So it will print the Index of Maharana not the Mr.That is the Exception here.

# isalpha() :- String Having (A-Z, a-z)
Str12 = "Sneha"
print(Str12.isalpha())#(Return Boolean)

# isalnum() :- String Having (A-Z, a-z, 1-9)
Str12 = "Sneha"
print(Str12.isalnum())#(Return Boolean)
Str13 = "Sneha001"
print(Str13.isalnum())#(Return Boolean)

# isprintable()
Str14 = "Hello boy how is coding jorney is Going"
print(Str14.isprintable())#It will tell that all the element in the string is printable or not. (Return Boolean)
Str15 = "Hello Adarsh\nGood Morning\tHave your Breakfast?"
print(Str15.isprintable())#If String has any Escape Sequence then it will print false (Return Boolean)

# isspace
Str16 = "    "
print(Str16.isspace())#If the String contains only white space(Wide Space) (Return Boolean)

# istitle()
Str17 = "The Man Of Wrds"
print(Str17.istitle())#If the first letter of each word of the string is capitalized.(Retrun Boolean)

# tile()
Str18 = "hello world tO ProGramming"
print(Str18.title())#Capitalized all the First letter of each word of the String. 

# strip()
Str19 = "!!   hello world   !!"
print(Str19.strip("!"))#remove leading and trailing character.
Str19a = "   Hello World   "
print(Str19a.strip())#remove leading and trailing spaces also.

# join()
Str20 ="Hello", "Adarsh", "Singh"
print(" ".join(Str20))#It Basically join the string seperated with comma.
