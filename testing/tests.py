import json
import requests

# rn this is just requesting existing microservices,
# need to add creation and deletion of services

def test_microservice(endpoint, parameters=None):

    base_url = 'http://127.0.0.1:34225'
    url = f'{base_url}/{endpoint}'

    # Make a request with parameters
    # try except
    response = requests.get(url, params=parameters)

    # Check the response
    print(f"Testing request on {url} with parameters: {parameters}")

    if response.status_code == 200:
        print("Request was successful")

        # https://www.w3schools.com/python/ref_requests_response.asp

        print("Response body:", response)
    else:
        print("Request failed")
        print("Status code:", response.status_code)

# Load test data from the JSON file
with open('tests.json') as json_file:
    tests = json.load(json_file)

# Run tests
for test in tests:
    test_microservice(test['endpoint'], test['parameters'])
