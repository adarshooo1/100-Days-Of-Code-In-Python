from Main import Tester


Human = Tester("Deepanshu")
print(Human.Name)

print(str(Human))
print(repr(Human))

# In case if we have the __str__ then it will print the __str__method else it will fall of to the __repr__.
print(Human)

# When we call the object associated with the class and class has the __call__ method then it will be run Ex:- Human = Tester(), then when we call Human() in the empty then it will call the function of __call__ and the value inside it.
Human()