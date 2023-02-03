import requests
import json
import jsonpath
# api url
url = "https://reqres.in/api/users"

# read input json file
file = open("C:/api automation/post_req.json" , "r")
json_input = file.read()

# converting into json format
request_json = json.loads(json_input)
print(json_input)

# make post request with json body input
response = requests.post(url , request_json)

print(response.content)

# validating response code

# assert response.status_code == 201

# fetch header from response
print(response.headers)

# if we want particular header details
print(response.headers.get("Content-length"))

# parse response to json format

response_json = json.loads(response.text)

# pick id using jsonpath
id = jsonpath.jsonpath(response_json , "id")
print(id[0])

