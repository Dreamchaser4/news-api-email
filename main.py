import requests
from send_email import send_email

api_key ="3080d4ade206453db6e996e571e5cd1e"
url = "https://newsapi.org/v2/top-headlines?country=us&category=business&" \
      "apiKey=3080d4ade206453db6e996e571e5cd1e&language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""

for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject : Today's news" + \
               "\n" + body + article["title"] + "\n" \
               + str(article["description"]) \
               + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)