import requests
import json
import jsonpath
import pytest

def test_add_new_data():
    url = "https://reqres.in/api/unknown"
    file = open("C:/api automation/list_users.json" , "r")
    read = file.read()
    convert_json = json.loads(read)
    response = requests.post(url , convert_json)
    print(response.text)

    #tech_api_url = ""
    #file = open

