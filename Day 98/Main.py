# Import the required modules
import multiprocessing
import requests
import time

# Define a function to download a file from the given URL and save it with the given name
def downloadFile(url , name):
    response = requests.get(url)  # Send a GET request to the URL and get the response
    with open(f"files/file{name}_{int(time.time())}.jpg" , "wb") as f:  # Open a file with the given name and write the response content to it
        f.write(response.content)

if __name__ == '__main__':
    url = "https://picsum.photos/2000/3000"  # Set the URL of the file to download

    pros = []  # Create an empty list to store the process objects

    for i in range(5):
        # downloadFile(url , i)  # Download the file with the given URL and name
        download = multiprocessing.Process(target=downloadFile , args=[url , i])  # Create a new process to download the file
        download.start()  # Start the process
        pros.append(download)  # Add the process object to the list

    for download in pros:
        download.join()  # Wait for each process to finish downloading the file




# In this code, we first import the required modules - multiprocessing, requests, and time.

# We define a function called downloadFile() which takes in a URL and a name and downloads the file from the URL and saves it with the given name. This function is called by the child processes.

# We use the if __name__ == '__main__': clause to ensure that the code inside this block is only executed when the script is run directly and not when it is imported as a module.

# We set the URL of the file to download and create an empty list called pros to store the process objects.

# We then use a for loop to create 5 child processes, each of which calls the downloadFile() function with the given URL and index i as arguments. We start each process using the start() method and add the process object to the pros list.

# Finally, we use another for loop to wait for each process to finish downloading the file using the join() method. This ensures that all the files are downloaded before the script exits.

