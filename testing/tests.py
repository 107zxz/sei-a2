import sys
import json
import requests
import argparse

# flask run -p 3000
greetings_base = "http://127.0.0.1:3000/"
timestamp_base = "http://127.0.0.1:3000/"
dice_roll_base = "http://127.0.0.1:3000/"
input_validate_base = "http://127.0.0.1:3000/"
calculate_base = "http://127.0.0.1:3000/"
format_output_base = "http://127.0.0.1:3000/"

# TODO: add output comparisons

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
    print(f"\nRequesting: {url} with parameters: {parameters}")

    # Try making a request to url endpoint
    try:
        response = requests.get(url, params=parameters)
        print("Status code:", response.status_code)
        print("Response body:", response.content)

    except Exception as e:
        print(e)

parser = argparse.ArgumentParser(description='Run test cases against existing microservices.')
parser.add_argument('--bypass', action='store_true', help='Bypass gateway and directly query microservices')
args = parser.parse_args()

# Load test data from the JSON file
with open('tests.json') as json_file:
    tests = json.load(json_file)

# Run tests
base = ""
for test in tests:

    if args.bypass:

        if test['endpoint'] == "noncomm/greetings":
            base = greetings_base
        elif test['endpoint'] == "noncomm/timestamp":
            base = timestamp_base
        elif test['endpoint'] == "noncomm/dice_roll":
            base = dice_roll_base
        elif test['endpoint'] == "comm/increment": # input_validate
            base = input_validate_base
        elif test['endpoint'] == "comm/inc-calculate":
            base = calculate_base
        elif test['endpoint'] == "comm/inc-format-output":
            base = format_output_base

        test_microservice(None, test['parameters'], base)    

    else:
        test_microservice(test['endpoint'], test['parameters'])    

