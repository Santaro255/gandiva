#!/usr/bin/python
# encoding: utf-8
import requests
import json
import sys

# params
gandiva_user = "domain\\user"  # changeme
gandiva_pass = "password"  # changeme
gandiva_api_url = "https://api-address/"  # changeme
body = sys.argv[1]


# token part
def gandiva_get_token():
    headers = {'Content-Type': 'x-www-form-urlencoded'}
    data = {
        'grant_type': 'password',
        'username': gandiva_user,
        'password': gandiva_pass
        }
    response = requests.post(gandiva_api_url + "Token", data=data, headers=headers)
    return response.json()['access_token']


gandiva_api_key = gandiva_get_token()

token = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + gandiva_api_key
    }


# create request
def main():
    data = {
        'Department': {'Id': 1, 'Name': 'Department name'},  # changeme
        'Category': {'DepartmentId': 1, 'Id': 10, 'Name': 'Category name'},  # changeme
        'RequestType': {'CategoryId': 10, 'Id': 100, 'Name': 'Request type name'},  # changeme
        'JobType': {'Id': 200, 'Name': 'Job type name', 'RequestTypeId': 100},  # changeme
        'Description': body,
        #'CustomFields': [{'CustomFieldId': 300, 'Value': ' ', 'ValueId': None}] # changeme if field required or remove
        }
    requests.post(gandiva_api_url + "api/Requests", data=json.dumps(data), headers=token)


# run
if __name__ == "__main__":
    main()
