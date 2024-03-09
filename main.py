import requests

from send_email import send_email

api_key = "2b88f42ed0f64461bbddf78546cd0e98"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-02-09&sortBy=publishedAt&apiKey" \
      "=2b88f42ed0f64461bbddf78546cd0e98"

request = requests.get(url)

# Get data from API and put it into Dictionary
content = request.json()

message = "Subject: Test Mail API \n"

for article in content["articles"]:
    entry = (f"{article["title"]}\n"
             f"{article["description"]}\n")

    message += entry

print(message)

send_email(message)
