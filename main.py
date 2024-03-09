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

    # Add title to message
    entry = f"{article["title"]}\n"
    message += entry

    # Check if description is non NoneType otherwise .replace() will print bug
    if article["description"] is None:
        pass
    else:
        # Add description to message and remove excess break lines
        entry = f"{article["description"].replace('\n', '')}\n ------------------------------------ \n"

    message += entry

# Encode message to utf-8 to fix Bug
message = message.encode('utf-8')

print(message)

send_email(message)
