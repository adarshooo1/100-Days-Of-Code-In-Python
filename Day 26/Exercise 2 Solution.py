import time#Importing time will help you to get function related to time

# Way 1//////////////////////////////////

timestamp = (time.strftime('%H:%M:%S'))#Function to get time module in python which will print [Hour:Minute:Second]

Hour = int(time.strftime('%H'))#Converting Hour String to int Because,strftime() gives time in String. So we have to convert into Integer.

if(Hour > 12 and Hour <= 16 ):
    print(f"Good After Noon Sir time is:- {timestamp}")
elif (Hour > 16 and Hour <= 24):
    print(f"Good Evening Sir time is:- {timestamp}") 
else:
    print(f"Good Morning Sir time is:- {timestamp}") 


# Way 2//////////////////////////////////
import time

# Get the current hour and minute
hour = time.localtime().tm_hour
minute = time.localtime().tm_min

# Set the greeting
if hour < 12:
    greeting = "Good Morning"
elif hour < 18:
    greeting = "Good Afternoon"
else:
    greeting = "Good Evening"

# Print the greeting
print(f"{greeting} Sir, the time is {hour}:{minute}")