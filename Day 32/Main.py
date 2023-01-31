set1 = {1,2,3,4}
set2 = {5,6,7,8}
print(set1.union(set2))#It will print all the item present in set1 and set2

set1.update(set2)
print(set1)# It will add the itme of set2 in set1 and change the set item

set3 = {"India","America","London","Las-Vegas"}
set4 ={"India","America","Bejing","New-York"}
set5 = set3.intersection(set4)
print(set5)#It will print that value which is in both the set

set3.intersection_update(set4)
print(set3)#It will print the Item in set3 which is in both sets.


cities1 = {"Delhi","Noida","Panipat","Surat"}
cities2 = {"Delhi","Surat","Gt.Noia","Sutiyana"}

print(cities1.difference(cities2))#What are the values in cities1 are different form cities2:-That is Noida and Panipat
cities1.difference_update(cities2)
print(cities1)#Please Update the difference in cities1 and store the value
print(cities1.symmetric_difference(cities2))#It is taking the difference same and printing the complete value
cities1.symmetric_difference_update(cities2)
print(cities1)#it is updating the values of cities2 in the cities1.

print(cities1.isdisjoint(cities2))#It will return the Boolean Expressionz:- If the sets are completely different then print true else false.



country1 = {"India","Japan","China","Pakistan"}
country2 = {"India","Pakistan"}

print(country2.issubset(country1))#Is the element present in country2 are also in country1,So Yes all the element which is in country2 having in country1
print(country1.issuperset(country2))#Is country1 have the all the item of country2 as well as more than country2.So, True
print(country1.issubset(country2))#Is country2 have all the Objects of country1.Answer is False:- Country1 have more object than country2

country1.add("America")
print(country1)

country2.remove("India")
print(country2)#It will through error when element is not present so it can stop the program. So to prevent stoppage we use discard();

country1.discard("Argintina")
print(country1)#Argentina is not present but still program is running.So this function Basically prevent to stop the program

item = country1.pop()#This is a emptry function which can pop or remove any item form the set randomly.
print(item)#To see what item get removed using this.
print(country1)#Now print the update country1

del country1
print(country1)#It will through error because now country1 is deleted and not existed anymore so useless to print.