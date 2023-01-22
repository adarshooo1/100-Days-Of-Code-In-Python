file = open('readlines().txt','r')
while True: #If the line in the txt file will present then it will statisfy the condition.
   line = file.readline() # Then it will print the line
   print(line)
   if not line: # If this conditions true then it will not print and break the loop.
      break # Program end.
     # readline will return string.

# readlines() Example
file3 = open('readlines3.txt','r')
i = 0
while True:
  i += 1
  line3 = file3.readline()

  if not line3:
    break
  m1 = line3.split(",")[0]#Here we are seprating commas and Indexing 
  m2 = line3.split(",")[1]
  m3 = line3.split(",")[2]
  print(f"Marks of student {i} in Maths is: {m1}")
  print(f"Marks of student {i} in Scinece is: {m2}")
  print(f"Marks of student {i} in English is: {m3}")

# writelines() Method
file4 = open('writelines.txt','w')
line4 = ['Hello Adarsh\n', 'How are you\n','What are you doing']
file4.writelines(line4)
file4.close()

# Sort way to write in a file
with open('example.txt', 'w') as file:
    lines = file.writelines("Python is very slower language than java")

# Sort way to read a file
with open('example.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
      print(line)