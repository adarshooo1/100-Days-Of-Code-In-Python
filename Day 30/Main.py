# Factorial Number
def factorial(n):
  if(n == 1 or n == 0):
    return 1
  else:
    return n * factorial(n-1)
print(factorial(5))


# Fionacci series

def fibonacci(n):
    if (n < 2):
        return n
    else:
     return fibonacci(n-1)+fibonacci(n-2)#Here function is calling another fuction to get the value

print(fibonacci(10))

# They both are the example are of type recursive in nature.