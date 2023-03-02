import requests
import json

Keyword = input("What type of news you are searching for?:")


# Here {Keyword will help in to search for the keyword that we are searching for. Example :-Tennis, cricket , weather , Scores}
url = (f'https://newsapi.org/v2/everything?q={Keyword}&apiKey=947f9aac75f94be0a32366e2a4d837b6')
response = requests.get(url)

# Here, response.text is a JSON-formatted string, and json.loads(response.text) converts that string into a Python object so that you can access and manipulate its contents more easily. The resulting Python object will typically be a dictionary, list, or a combination of both, depending on the structure of the JSON data.
news = json.loads(response.text)

# Here article is the array in the news api and it helps to fetch the title and description form that array, because in the array data is stored in the form of Dictionary type<Dict>
for News in news["articles"]:
    print(News["title"])
    print(News["description"])
    print("------------------------------------------------------------------")