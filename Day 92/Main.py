import functools
import time

@functools.lru_cache(maxsize=None)
def fx(n):
    # time.sleep will make the system respond after 5 sec later.
    time.sleep(4)
    return n*5

# or
# from functools import lru_cache
# lru_cache(maxsize = none)

print(fx(20))
print("Done for 20")
print(fx(2))
print("Done for 2")
print(fx(12))
print("Done for 12")
print(fx(22))
print("Done for 22")

# This is already store in the lru_cache so it will not take time to computer again it just take the value match the value if
# same then print the already same existing answer else it will have to computer then print the answer and store the value of
# the next time if the same value is again come back.(simply store the Data and if needed then it returns). It Memoize the value,
# Which take the space to store the value and once the program again run then it will clear the past store cache and again start filling cache as a new.
print(fx(20))
print("Done for 20")
print(fx(2))
print("Done for 2")
print(fx(4))
print("Done for 4")
print(fx(22))
print("Done for 22")