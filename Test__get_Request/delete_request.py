import requests
import json
import jsonpath

# api url
url = "https://reqres.in/api/users/2"

# delete
response = requests.delete(url)

# fetch response code

print(response.status_code)

# validating
assert response.status_code == 204