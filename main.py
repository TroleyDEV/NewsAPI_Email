import requests

from send_email import send_email

api_key = "2b88f42ed0f64461bbddf78546cd0e98"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-02-09&sortBy=publishedAt&apiKey" \
      "=2b88f42ed0f64461bbddf78546cd0e98"

request = requests.get(url)

# Get data from API and put it into Dictionary
content = request.json()

# Construct title for Email message
message = "Subject: Test Mail API \n"

for article in content["articles"]:

    # Add title to message and check if NoneType
    if article["title"] is None:
        entry = "--- No Title ---"
    else:
        entry = f"{article["title"]}\n"

    message += entry

    # Add description and check if NoneType
    if article["description"] is None:
        entry = "--- No Description ---"
    else:
        entry = f"{article["description"].replace('\n', '')}\n ------------------------------------ \n"

    message += entry

# Encode message to utf-8 to fix Bug
message = message.encode('utf-8')

print(message)

send_email(message)
