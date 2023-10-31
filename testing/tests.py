import json
import requests

# TODO: fill these in 
greetings_base = ""
timestamp_base = ""
dice_roll_base = ""
input_validate_base = ""
calculate_base = ""
format_output_base = ""

def format_url(endpoint, base_url):

    # no endpoint, direct request
    if endpoint == None:
        url = base_url

    # endpoint given, request through gateway
    else:
        url = f'{base_url}/{endpoint}'
    
    return url

def test_microservice(endpoint, parameters=None, base_url='http://kube.info'):

    url = format_url(endpoint, base_url)

    # Check the response
    print(f"Requesting: {url}")

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

