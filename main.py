import requests


api_key ="3080d4ade206453db6e996e571e5cd1e"
url = "https://newsapi.org/v2/top-headlines?country=us&category=business&" \
      "apiKey=3080d4ade206453db6e996e571e5cd1e"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
