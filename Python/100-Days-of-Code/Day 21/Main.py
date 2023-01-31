# # Default Argument:
# def Name(fname = "Siya",mname = "Ram",lname = "Chandra"):#This is a default function which will print this automaticall when user will not enter his name.
#     print("Mr./Mrs. ",fname,mname,lname)

# Name("Adarsh","Kumar","Singh")
# Name(mname="Kumar",lname="Singh")
# Name(fname="Hanuman")#Here we are giving value to fname only and it is print mname and lname also Because of Default program



# # Keyword Arguement
# def Name2(lname,mname="Null",fname ="Null"):
#     print("Hello",fname,mname,lname)

# Name2(mname="Singh",fname="Deepanshu",lname="Chauhan")#By the keyword fname,mname,lname we are calling the function and passing the objects so that program can easy to run and maintain
# # Example: In a School when the time for lunch then many mother came to the school to give lunch to their child.If their is no keyword that can tell children lunch information So,
# # Mother Write names in the lunch which is a keyword and child can understand whose lunch is this in lunch time. 


# # Variable Length Argument
def  AvgofNums(*Numbers):
    nums = 0
    for i in Numbers:
        nums += i
    print("The Average is",nums /len(Numbers))

c = AvgofNums(10,20)
print(c)#Here the velue of c in None.Because in Function it itself printing the value not storing.It so if we
# want to store then have to write return statement and then it will print

        
# # Required Argument
# def Average(a,b=0,c=0):#Here a is the required argument
#     print("The Average is",(a+b+c)/3)
