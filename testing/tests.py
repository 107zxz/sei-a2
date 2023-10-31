import json
import requests

# rn this is just requesting existing microservices,
# add creation and deletion of services? or manual

def test_microservice(endpoint, parameters=None):

    base_url = 'http://127.0.0.1:36107/'
    url = f'{base_url}/{endpoint}'

    # Check the response
    print(f"Testing request on {url} with parameters: {parameters}")

    # Try making a request to url endpoint
    try:
        response = requests.get(url, params=parameters)

        if response.status_code == 200:
            print("Request was successful")

            # https://www.w3schools.com/python/ref_requests_response.asp

            print("Response body:", response.content)
        else:
            print("Request failed, status code:", response.status_code)

    except requests.exceptions.RequestException as e:
        raise SystemExit(e)


# Load test data from the JSON file
with open('tests.json') as json_file:
    tests = json.load(json_file)

# Run tests
for test in tests:
    test_microservice(test['endpoint'], test['parameters'])
