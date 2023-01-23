# All this is the example of Lambda functions

# Lambda function of print square.
double = lambda x: x*x
print(double(4))

# Lambda function of print cube.
cube = lambda y: y**3
print(cube(5))

# Lambda function of print sum of 2 numbers.
sum = lambda x,y : (x+y)
print(sum(2,3))

# Lambda function of print average of 2 numbers.
average = lambda x,p : (x+p)/2
print(average(10,15))

# Question is, Can we pass a functions as a function inside a function.Answer is Yes.
def Cubeing(x , num):
    return 10 +x(num) 
print(Cubeing(cube,2))# Here we have a cube function alright and we initialize a value by 2.
#  What is happening in this cunning function: Let's check
#  Cubbing (cube , 2)
#  x = cube and num = 2; cubbing(x(cube) , num(2))
#  return 10 + (cube(num));
#  return 10 + (cube(2));
#  return 10 + (8);
#  return 18;

