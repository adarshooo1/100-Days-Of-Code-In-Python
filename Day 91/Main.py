# Example 1:
def a_gererator():
    for i in range (1 , 100):
        # yield is a keyword which will suspend the execution untill the special value isn't called.
        yield i


gen = a_gererator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))



# Example 2
def my_generator():
    yield 1
    yield 2
    yield 3

# This will print all the values in the my_generators().In a iteratable form and print all together in a sequence.
gen = my_generator()
for value in gen:
    print(value)

# This will print all the values when constructor Instance will be called. It also work as the same till the print (next(gen)) will not be called.
gen = my_generator()
print(next(gen)) # Output: 1
print(next(gen)) # Output: 2
print(next(gen)) # Output: 3





# Overall :- This generator isn't store the value in itself, That is the biggest usecase.


