
list = [1,2,3,4,5,6]
list.append(7)#append() Methods will add this 7 in the list and list get mofified
print(list)

list2 = [11,2,5,3,5,9,14]
list2.sort()#It will sort a randomly arranged list in a ascending sorted list
print(list2)

list3  = [20,43,2,0,12,14,8,23,11,14,15]
list3.sort(reverse=True)#This sort(reverse=True) will sort a randomly arranged list in a Descending Ordered list
print(list3)

list4 = [1,2,3,4,5,6,7,8]
list4.reverse()#This reverse() method just invert:-A to Z from Z to A the whole list
print(list4)

list5 = [1,2,3,4,5,6,7,8]
print(list5.index(5))#This index will return the index of any number in the list.If the Item will not be in the list then it will return error in program

list6 = [1,2,3,2,1,2,3,4,5,6,7,4,3]
print(list6.count(2))# Count will return the number of occurance of a number

list7 = [2,4,6,8,10,12,14,16]
print(list7)
list8 = list7
list8[0] = 1#Here we make change is list8 but it automatically pointing to list7,So any changes in list8 will directly affect it.So to prevent this we use copy function.
print(list7)

list9 = [1,2,3,4,5]
print(list9)
list10 = list9.copy()#Here any changes to list10 will not affect list9 because of copy methods
list10.append(6)
list10[2] = 10
print(list10)

list11 = [1,3,5,7,9,11,13]
print(list11)
list11.insert(2,12)#Here it will insert 12 at index 2.
print(list11)

list12 = ["Apple","Mango","Grapes"]
list13 = ["Apple","Mango","Grapes","Pineapple"]
list12.extend(list13)#Here extend function simply says open list12 and add list13 into it
print(list12)

list14 = list12 + list13
print(list14)#It will not make any chnages to the list12 and list13.

for num in list14:
    print(num,end=" ")#Using for loop to iterate items in list
