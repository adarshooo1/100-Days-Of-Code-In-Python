# Shout out to everyone.

# This line imports the pyttsx3 library, which is a Python text-to-speech library.
import pyttsx3

# This line defines a list of names.
Name_list = ["Adarsh" , "Deepanshu" , "Sopnil" , "Abhishek" , "Praneet" , "Anku" , "Rittik"]

# This line initializes a new instance of the pyttsx3 engine.
engine = pyttsx3.init()

for name in Name_list:

    # Prints the name to the console using the print() function.
    print(name)

    # Uses the engine.say() method to generate speech output for the name, with a greeting of "Hi" followed by the name.
    engine.say("Hii" + name)

    # Uses the engine.runAndWait() method to wait for the speech output to finish before moving on to the next name.    
    engine.runAndWait()
    