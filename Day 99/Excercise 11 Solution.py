import time  # importing the time module for time-related functions
import pyttsx3  # importing the pyttsx3 module for text-to-speech conversion
from win10toast import ToastNotifier  # importing the ToastNotifier module for displaying notifications on Windows 10

toaster = ToastNotifier()  # creating an instance of the ToastNotifier class
engine = pyttsx3.init()  # creating an instance of the pyttsx3 engine

while True:
    # displaying the notification to drink water
    toaster.show_toast("Drink Water Reminder", "It's time to drink water!")
    
    # converting the text to speech
    engine.say("It's time to drink water!")
    engine.runAndWait()
    
    # waiting for 1 hour before showing the next notification
    time.sleep(3600)

