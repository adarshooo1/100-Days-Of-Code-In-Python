# To create a empty dictionary
dict1 = {}
print(type(dict1))

# to create a dictionary of Integer values
dict2 = {'A':1,'B':2,'C':3}
print(dict2)

# To create a Dictionary of String
dict3 = {
    'Name':"Adarsh",
    20:"Age",
    'Sports':"Volley-ball"
}
print(dict3)#Like this way we can print the complete Dictionary
print(dict3['Name'])#Like this way we can access a single object in the Dictioary
print(dict3[20])#Like this way we can access string value stored in a integer object

Employee_Id = {
    1:"Sanjay",
    2:"Ranjana",
    3:"Adarsh",
    4:"Sneha"
}
print(Employee_Id[3])# If the element is present in the Dictionay then it will print the Item
# print(Employee_Id[5])# If the Key that we are accessing is not in Dictionary than Through Error.
print(Employee_Id.get(1))# It will also help in to access the key item.
print(Employee_Id.get(6))# If the key is not in the dictionary then it will print= None. as a key item. without error and stoppage of program

print(Employee_Id.keys())#it will return the key of the Dictionary with the help of [--Text--.keys()] function.

for key in Employee_Id:
    print(Employee_Id[key])# Like this way we can iterate over the dictionary keys and print items that the key stored in it.
    print(f"The Employee Id is {key} and the item is:- {Employee_Id[key]}")

print(Employee_Id.values())# It will return the values of the Dictionary stored in the Key.   


Roll_No = {
    "Adarsh":1,
    "Aman":2,
    "Baani":3,
    "Deepanshu":4,
    "Gaurav":5,
    "Harsh":6,
    "Sopnil":7,
    "Vivek":8
}
print(Roll_No.items())#Hete the function item will return the key and its value together. Ex:- ([('Adarsh',1), ('Aman',2)])

for Name, Roll in Roll_No.items():#Here we are iterating over the dictionary with diving name of key and its item to print easily.
    print(f"The Name is the Student is {Name} and the Roll Number is {Roll}")