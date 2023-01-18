Emp_id = {121: 40, 122:45, 123:50, 124: 55, 126:70}
Emp_id2 = {131: 65, 132: 75, 133:80}

Emp_id.update(Emp_id2)
print(Emp_id)#Here Emp_Id is updating the values of Emp_id2 in it.So, there is no need to print both seperately

Emp_id2.clear() # Clear Method will clear items in the dictionary.
print(Emp_id2) # Now It will print a empty Dictionary 

Fruit = {'Fruit1':"Apple",'Fruit2':"Mango",'Fruit3':"Grapes",'Fruit4':"Pine-Apple"}
Fruit.pop('Fruit4')#Pop() method will remove the item which we want from the Dictionary.
print(Fruit)

Fruit.popitem()# popitem() is a default method which will delete or remove the last element of the Dictionary
print(Fruit)

Fruit['Fruit3'] = "Litchi" #This will add the key and vlaue pair in the Dictionary
print(Fruit)

del Fruit['Fruit1']
print(Fruit)#This will delete the Key and will not print further

del Fruit
print(Fruit)#This will delete the Entire Dictionary and later if we call the Dictionary then It will give error. If we dont give a key value.