import os

print(os.getcwd())#This will tell the current directory we are working in.

print(os.chdir())

if(not os.path.exists("OS MODULE INTRO")):#This conditional will help in any
    os.mkdir("OS MODULE INTRO")


for i in range(1,100):
    os.rmdir(f"C:/Users/Adarsh Singh/Desktop/OS MODULE INTRO/Day {i+1}")#This os methods os.mkdir() is able to make multiple Directory with he help of for loop.

for i in range(1,100):
    os.rmdir(f"C:/Users/Adarsh Singh/Desktop/OS MODULE INTRO/Day {i+1}/python Main.py")#This os methods os.rmdir() is able to remove Directory files if having the same name.

