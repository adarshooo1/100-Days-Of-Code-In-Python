import requests              # Import the 'requests' module to make HTTP requests
from bs4 import BeautifulSoup  # Import the 'BeautifulSoup' module for parsing HTML

# Example 1: Sending a GET request to a website and printing its HTML content
response = requests.get("https://www.google.com")
# Use the .text attribute of the response object to get the HTML content as a string
print(response.text)


# Example 2: Sending a POST request to a website with some data
url = "https://jsonplaceholder.typicode.com/posts"
# Define a dictionary 'data' with some data to be sent with the request
data = {
    "title": 'foo',
    "body":'bar',
    "userId":1
}
# Define a dictionary 'headers' with some headers to be sent with the request
headers = {
    'Context-type': 'application/json: charset=UTF-8'
}
# Use the requests.post() method to send the POST request with the data and headers
response = requests.post(url , headers=headers , json=data)
# Use the .text attribute of the response object to get the response content as a string
print(response.text)


# Example 3: Scraping data from a website using BeautifulSoup
url = "https://www.nike.com/in/t/force-1-lv8-2-younger-shoes-TlkrLd/DV1623-001"
# Use requests.get() method to get the HTML content of the website
r = requests.get(url)
# Use the .text attribute of the response object to get the HTML content as a string
print(r.text)

# Use BeautifulSoup() constructor to parse the HTML content and create a BeautifulSoup object
soup = BeautifulSoup(r.text, "html.parser")
# Use findAll() method to find all the 'h2' tags in the HTML content and print their text
for h2 in soup.findAll("h2"):
    print(h2.text)

# Use prettify() method to format the HTML content in a human-readable way and print it
print(soup.prettify())

