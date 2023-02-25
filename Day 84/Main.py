# To access time module we have to import the time module:
import time


def usingWhile():
    i = 0
    while( i < 1000):
        i+= 1
        print(i)

def usingFor():
    for i in range(1 ,1000):
        print(i)


init = usingFor()
init = usingWhile()


# time.time() is a method in the time module.

start_time = time.time()

end_time = time.time()

execution_time = end_time - start_time
print("Execution time:", execution_time, "seconds")
# output :- Execution time: 0.0 seconds (time starts from 0)

init = time.time() 
usingFor()
t1 = time.time() - init
init = time.time()
usingWhile()
print(time.time() - init) #first this will print and it will take 0.031374454498291016 sec to run which is for the while loop.
print(t1) #then this will print and it will take 0.04116702079772949 sec to run which is for the for loop.

# time.sleep() is a method in the time module.

print(10)

time.sleep(5) #Here time.sleep(5) will take 5 sec and it will make program stop for 5 seconds then it will print the further lines.
print("This is printed after 3")

# time.strftime() is a method in the time module.


t = time.localtime()
print(t)
# output :- time.struct_time(tm_year=2023, tm_mon=2, tm_mday=25, tm_hour=22, tm_min=54, tm_sec=26, tm_wday=5 , tm_yday=56, tm_isdst=0)


# for printing (Year-Month-Day) then print ("%Y-%m-%d") for printing(Hour:Minute:Sec) then print (" %H:%M:%S")
formatted_time = time.strftime("%Y-%m-%d  %H:%M:%S",t)
print(formatted_time)


# time.ctime() is a method in the time module.

current_time = time.ctime()
# This will tell the current time with the weekname, day , time and year. Whatever in the current.
print("Current time:", current_time)






