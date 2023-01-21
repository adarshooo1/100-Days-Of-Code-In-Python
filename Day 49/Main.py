# NOTE This may can Happen that it might noy working in VS.code Same in My case so Please Try this in a (online)IDE like Replit. https://replit.com/@adarshooo1

# Example 1:
file = open('myfile.txt','r') # Here myfile.txt is already a file which we are trying to open insdie a open functions where 'myfile' is the file names and 'r' means read

# print(file)

# This is for reading a file
text = file.read()
print(text)
file.close()

#Example 2:
# This for writting a file.
file2 = open('myfile.txt','a') # Here, 'a' refers to append if we place 'w' then we can also write but the previos txxt will delete automatically.
text2 = file2.write(
  "\nThis is about IO file"
)  # This will apeend the text without deleting the other word
file2.close()

#Example 3:
file3 = open("myfile2.txt",'w') 

#If by chance we have no such file like file3 and we still want to wriye this then it will automatically create a file then it will write else it will write.
#If we will not append 'a' then it will write the message, But concequences is It will delete or remove the previous written things

#As more and more we run the file it will append the same thing

text3 = file3.write('This is file 4')
file3.close() # This is mandatory to save the text or make changes in the file with the help of IO modes in Pytton

# Example 4:
with open("myfile3.txt",'a')as text4:
  text4.write("\nThis is myfile4.txt")
#Short way to do

#Exmple 5:
#This is for reading in Binay form
# Open a binary file in read mode
with open('myfile4.txt', 'rb') as f:
# Read the contents of the file
# With helps in close() as Default
  data = f.read()
  print(data)

# Example 6: 
# Try to open a file in exclusive creation mode
try:
    with open("myfile5.txt", "x") as f:
        # Write some data to the file
        f.write("Hello, World!")
# This will exclusively make a file and it is there then it will through exception : Else create a new file named with new_File.txt.
except FileExistsError:
    print("File already exists.")



  

  