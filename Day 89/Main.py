import requests

from bs4 import BeautifulSoup

# response = requests.get("https://www.google.com")

# # .text method will print the google website in the string format when we request
# print(response.text)



# url = "https://jsonplaceholder.typicode.com/posts"

# data = {
#     "title": 'foo',
#     "body":'bar',
#     "userId":1
# }

# headers = {
#     'Context-type': 'application/json: charset=UTF-8'
# }

# response = requests.post(url , headers=headers , json=data)

# print(response.text)

# # For-scrapping we use (Bs4) module named BeautifulSoup;


url = "https://www.nike.com/in/t/force-1-lv8-2-younger-shoes-TlkrLd/DV1623-001"

r = requests.get(url)
print(r.text)

soup = BeautifulSoup(r.text, "html.parser")

for h2 in soup.findAll("h2"):
    print(h2.text)

