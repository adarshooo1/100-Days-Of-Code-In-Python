# # import math
# import math

# # Floor (Base Number)
# numb1 = math.floor(87.9233)
# print(numb1)#It will round off the value and print the minimum value if the number in decimals
# # Ceiling (Max Number)
# numb2 = math.ceil(87.33)
# print(numb2)#It will round off the value and print the maximum value if the number in decimals


# # This math module perform mathematical opeerations
# result = math.sqrt(9)
# print(result) # Output = 3.0


# # Keyword in import
# from math import sqrt,pi #(imported square root and pie from maths module not other unecesssary functions which is keyword.)

# result2 = sqrt(81) * pi # Sqrt means square-root of 81 that is 9 and Pi means pie of mathematics 3.141592653589793
# print(result2)

# # * This will import everything from the math module. which is not suggested and recommended
# from math import *
# result3 = sqrt(25)
# print(result3)

# print(pi)

# # # The "as" Keyword
# import math as m  #m help in calling a functions with the help of as Keyword.
# result4 = m.sqrt(21) * m.pi
# print(result4)

# from math import pi as p,sqrt as sq #Here from math module we import sqrt which is defined as sq and pi which is defined as p. This will help progammer to not to write complete functions name and in shortcut we can define it.
# result5 = sq(675)*p
# print(result5)

# # # The dir functions.
# # As the math module is already imported then we can check that how many function is there inside the math module.
# print(dir(math)) 
#      # ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos'
#      # , 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', '
#      # comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc'
#      # , 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp'
#      # , 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf
#      # ', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p',
#      #  'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radi
#      # ans', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc'
#      # , 'ulp']

#  # All this are the function of math module.

# print(math.exp2, type(math.exp2))
# print(math.nan, type(math.nan))


# Here We Created a py file with some functions
import Greeting
Greeting.greet(f"Adarsh")

from Greeting import greet , Message
print(Message)

# Note:- There might be some problem to not to able to do in a offline code editor so after creating a function run that file
# then import the function. In this process it will make a file.But that is ok.