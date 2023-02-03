import requests
import json
import jsonpath


# app url
url = "https://reqres.in/api/users/2"

# read input jsonfile
file = open("C:/api automation/put_req.json" , "r")
json_input = file.read()

# converting file to json file
request_json = json.loads(json_input)
print(request_json)

# put request
response = requests.put(url , request_json)

# fetch response code
print(response.status_code)

# validating the response

assert response.status_code == 200


# parse response content
response_json = json.loads(response.text)
updated = jsonpath.jsonpath(response_json , "updatedAt")
print(updated[0])
