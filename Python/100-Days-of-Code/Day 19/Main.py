# Break Statement
for nums in range(1,14):#Here it is printing table till range of (n-1) which is 13 here.
    # So, Suppose we want to print the table till range of 10 and then exit the loop with the help of Break.So we can do like this
    if nums == 11:
        break
    print(f"2 X {nums} = {2*nums}")
print("Loop Exit")

# Continue Statement
for nums2 in range(1,15):
    if(nums2 == 10):
        print("Iteration Skipped")
        continue
    print(f"5 X {nums2} = {5*nums2}")

# Break and Continue :- Example 1
for nums3 in [1, 2, 3, 4, 5]:
    if nums3 % 2 == 0:
        continue  # skip the rest of the current iteration
    if nums3 == 4:
        break  # exit the loop
    print(nums3)

# Break and Continue :- Example 2
nums4 = 1
while nums4 <= 5:
    if nums4 % 2 == 0:
        nums4 += 1
        continue  # skip the rest of the current iteration
    if nums4 == 4:
        break  # exit the loop
    print(nums4)
    nums4 += 1    

