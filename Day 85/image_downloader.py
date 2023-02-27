# Importing necessary modules

# Inbuit module
import argparse  # Module for parsing command-line arguments
import os        # Module for interacting with the operating system

# pip install requests
import requests  # Module for sending HTTP requests
from urllib.parse import urlparse  # Module for parsing URLs

# Creating an instance of ArgumentParser class
parser = argparse.ArgumentParser(description="Online Image Downloader")

# Adding command-line arguments to the parser, as well he have also type argument which will take the datatype of the input.
parser.add_argument("url",type=str, help="Paste url to download Image")  # Required positional argument for image URL

parser.add_argument("-n", "--name", help="Save your image Name", default="Random_Image")  # Optional argument for image name

# Parsing the command-line arguments
args = parser.parse_args()

# Sending an HTTP GET request to the image URL
response = requests.get(args.url)

# Checking if the response status code is 200 (OK)
if response.status_code == 200:
    # Parsing the URL to extract the file extension
    parsed_url = urlparse(args.url)
    _, ext = os.path.splitext(parsed_url.path)

    # Checking if the file extension is valid (i.e., one of the supported image formats)
    if ext.lower() not in [".jpg", ".jpeg", ".png", ".bmp", ".gif", ".webp"]:
        ext = ".jpg"  # Setting a default file extension of ".jpg" if the provided URL does not specify a valid extension

    # Generating a unique filename for the downloaded image
    filename = f"{args.name}{ext}"

    # If dowload more then 1 image without name then it will rename as random1 , random2 ..etc, With the help of count. 
    i = 1
    while os.path.exists(filename):
        filename = f"{args.name}{i}{ext}"
        i += 1

    # Writing the contents of the HTTP response to a file with the generated filename
    with open(filename, 'wb') as f:
        f.write(response.content)

    # Printing a success message with the filename of the downloaded image
    print(f"Image downloaded successfully as {filename}.")
else:
    # Printing an error message if the response status code is not 200
    print("Failed to download image. Error code:", response.status_code)
