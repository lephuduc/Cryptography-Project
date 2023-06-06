import requests

api_url = "http://aboutservice.internal:5001/api/getAbout"
response = requests.get(api_url)

print(response.json())
