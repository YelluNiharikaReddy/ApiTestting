import requests
import json
import jsonpath

# api url
url = "https://reqres.in/api/users?page=2"

# send request
response = requests.get(url)

# response content
print(response.content)


# parse response in json format

json_response = json.loads(response.text)
print(json_response)

# fetch value using json path
pages = jsonpath.jsonpath(json_response , "total_pages")
print(pages[0])
