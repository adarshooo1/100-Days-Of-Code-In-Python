# Example 1.Where when loop ended then it gives control to else-Conditional.
for i in range(10):
    print(i)
else:#Here we can clearly see that without using if-conditional we can use else statement,
    # Its Because when loop ends. It loose the control then it ends the program and print the else 
    print("Loop Completed") 


# Example 2.Here when loop is terminated because of Break statement and program end and not goes further.
for num in range(10):
  if(num != 6):
    print(num)
 #Here the loop is successfuly completed and End-up the program and not execute further
  else:
    print("Loop Completed")#Here it not Executing because of break statement before this line;
    break
    

# Example 3.
for numb in range(10):
    print("Iteration no {} in for loop".format(numb+1))#Other way:-print(f"Iteration no {numb+1} in for Loop")
else:
    print("Else Block in Loop")   
print("Out of Loop")  