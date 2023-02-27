import argparse
import os
import requests
from urllib.parse import urlparse

parser = argparse.ArgumentParser(description="Online Image Downloader")

parser.add_argument("url" , help="Paste url to download Image")
parser.add_argument("Image_Name" , help="Save your image Name" , default="Random Image")

# Parse the arguments.
args = parser.parse_args()

# Download the image using requests.
response = requests.get(args.url)

# Check if the request was successful (status code 200).
if response.status_code == 200:
    # Extract the file extension from the URL.
    parsed_url = urlparse(args.url)
    _, ext = os.path.splitext(parsed_url.path)

    # If the file extension is not supported, use JPEG as the default.
    if ext.lower() not in [".jpg", ".jpeg", ".png", ".bmp", ".gif", ".webp"]:
        ext = ".jpg"

    # Save the image to a file with the appropriate extension.
    filename = f"{args.Image_Name}{ext}"
    with open(filename, 'wb') as f:
        f.write(response.content)
    print(f"Image downloaded successfully as {filename}.")
else:
    print("Failed to download image. Error code:", response.status_code)
