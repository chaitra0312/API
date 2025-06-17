import requests
url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title":"Hello lucky!",
    "body": "Chaitra is good ",
    "userID" : 1
}
response = requests.post(url, json=data)
if response.status_code == 201:
    print("Post success!")
    print("Response:" ,response.json())
else:
    print("Error occured:", response.status_code)
